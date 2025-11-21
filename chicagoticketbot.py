import time
import json
import os # <--- NEW: Needed to create folders
from playwright.sync_api import sync_playwright

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

    # --- NEW STEP: Create screenshots folder if missing ---
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
        print("Created 'screenshots' folder.")
    # ----------------------------------------------------

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500, channel="chrome")
        context = browser.new_context()
        context.set_default_timeout(120000) 
        page = context.new_page()

        for car in fleet_data:
            plate = car['plate']
            print(f"\n🚗 Processing: {plate}...")
            
            try:
                # Navigate & Fill Form
                page.goto("https://webapps1.chicago.gov/payments-web/#/home")
                page.locator(".card-container").filter(has_text="PARKING, RED LIGHT").locator("#Pay-button").click()
                page.get_by_role("tab", name="License Plate").click()
                
                page.locator("label:has-text('License Plate') + input").fill(plate)
                page.locator("label:has-text('State') + select").select_option(car['state'])
                page.locator("label:has-text('Last Name') + input").fill(car['company'])

                # Captcha Handling
                print("   > Waiting for Captcha...")
                page.wait_for_selector("iframe[src*='hcaptcha']", timeout=15000)
                captcha_frame = page.frame_locator("iframe[title*='Widget containing checkbox']")
                captcha_frame.locator("#checkbox").click()
                print("   > Checkbox clicked. Please solve the puzzle...")
                
                # Verification Loop
                while True:
                    try:
                        checkbox_fresh = captcha_frame.locator("#checkbox")
                        is_checked = checkbox_fresh.get_attribute("aria-checked", timeout=5000)
                        if is_checked == "true":
                            print("   ✅ Captcha Verified!")
                            break
                        time.sleep(0.5)
                    except:
                        time.sleep(0.5)
                        continue

                # Click Search
                print("   > Clicking Search...")
                page.get_by_role("button", name="Search").click(force=True)
                
                # Smart Wait & Screenshot
                print("   > Waiting for results...")
                try:
                    page.wait_for_load_state("networkidle", timeout=10000)
                except:
                    pass

                # --- UPDATED SCREENSHOT PATH ---
                filename = f"screenshots/Result_{plate}.png"
                page.screenshot(path=filename, full_page=True)
                print(f"   📸 Saved to: {filename}")
                # -------------------------------
                
                time.sleep(1)

            except Exception as e:
                print(f"   ❌ Error processing {plate}: {e}")
                # Save error screenshots to the folder too
                page.screenshot(path=f"screenshots/Error_{plate}.png")

        print("\n--- All cars processed. Closing browser. ---")
        browser.close()

if __name__ == "__main__":
    run_bot()