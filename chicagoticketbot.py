import time
import json
from playwright.sync_api import sync_playwright, TimeoutError

def run_bot():
    print("--- CHICAGO TICKET BOT (Manual Assist Mode v2) ---")
    print("Loading fleet.json...")
    
    try:
        with open('fleet.json', 'r') as f:
            fleet_data = json.load(f)
        print(f"Loaded {len(fleet_data)} vehicles.")
    except FileNotFoundError:
        print("Error: fleet.json not found.")
        return

    with sync_playwright() as p:
        # We launch the browser
        browser = p.chromium.launch(headless=False, slow_mo=500, channel="chrome")
        context = browser.new_context()
        
        # 1. INCREASE GLOBAL TIMEOUT
        # We give the bot 2 minutes (120000ms) before crashing, giving you plenty of time to solve puzzles
        context.set_default_timeout(120000) 
        
        page = context.new_page()

        for car in fleet_data:
            plate = car['plate']
            print(f"\n🚗 Processing: {plate}...")
            
            try:
                # Navigate
                page.goto("https://webapps1.chicago.gov/payments-web/#/home")
                
                # Select Parking Ticket
                page.locator(".card-container").filter(has_text="PARKING, RED LIGHT").locator("#Pay-button").click()
                
                # Switch to License Plate Tab
                page.get_by_role("tab", name="License Plate").click()
                
                # Fill Form
                page.locator("label:has-text('License Plate') + input").fill(plate)
                page.locator("label:has-text('State') + select").select_option(car['state'])
                page.locator("label:has-text('Last Name') + input").fill(car['company'])

                # --- CAPTCHA HANDLING (Robust Loop) ---
                print("   > Waiting for Captcha...")
                
                # Find the frame
                page.wait_for_selector("iframe[src*='hcaptcha']", timeout=15000)
                captcha_frame = page.frame_locator("iframe[title*='Widget containing checkbox']")
                
                # Click it
                captcha_frame.locator("#checkbox").click()
                print("   > Checkbox clicked. Please solve the puzzle...")
                
                # --- THE FIX: RE-CHECK ELEMENT INSIDE LOOP ---
                while True:
                    try:
                        # We re-locate the checkbox every single second.
                        # This prevents the "Stale Element" error if the iframe refreshes.
                        checkbox_fresh = captcha_frame.locator("#checkbox")
                        is_checked = checkbox_fresh.get_attribute("aria-checked", timeout=5000)
                        
                        if is_checked == "true":
                            print("   ✅ Captcha Verified!")
                            break
                        
                        # Small breathing room
                        time.sleep(0.5)
                    except Exception:
                        # If something glitches for a split second, ignore it and try again
                        time.sleep(0.5)
                        continue

                # 6. CLICK SEARCH (Forced)
                print("   > Clicking Search...")
                # force=True ensures we click even if the captcha popup is slightly overlapping the button
                page.get_by_role("button", name="Search").click(force=True)
                
                # 7. SMART WAIT & SCREENSHOT
                print("   > Waiting for results (Network Idle)...")
                
                # Instead of sleep(5), we wait until the network stops loading data.
                # This makes it fast (as soon as it's done) but safe.
                try:
                    page.wait_for_load_state("networkidle", timeout=10000)
                except:
                    # If networkidle times out (rare), we just proceed
                    pass

                filename = f"Result_{plate}.png"
                page.screenshot(path=filename, full_page=True)
                print(f"   📸 Screenshot saved: {filename}")
                
                # 8. Loop Reset
                time.sleep(1)

            except Exception as e:
                print(f"   ❌ Error processing {plate}: {e}")
                page.screenshot(path=f"Error_{plate}.png")

        print("\n--- All cars processed. Closing browser. ---")
        browser.close()

if __name__ == "__main__":
    run_bot()