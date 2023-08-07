import os
import pandas as pd
import requests

def take_screenshot(url, output_path):
    api_key = "YOUR_API_KEY"  # Replace with your apiflash API key
    screenshot_url = f"https://api.apiflash.com/v1/urltoimage?access_key={api_key}&url={url}"
    
    response = requests.get(screenshot_url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
            print(f"Screenshot saved for {url}")
    else:
        print(f"Failed to capture screenshot for {url}")

def main():
    input_excel_path = "input.xlsx"
    output_excel_path = "output.xlsx"
    df = pd.read_excel(input_excel_path)
    
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    for index, row in df.iterrows():
        url = row['Website']
        screenshot_path = f"screenshots/{url.replace('http://', '').replace('https://', '')}.png"
        take_screenshot(url, screenshot_path)
        df.at[index, 'Screenshot'] = screenshot_path
    
    df.to_excel(output_excel_path, index=False)
    print("Screenshots captured and saved to the output Excel file.")

if __name__ == "__main__":
    main()
