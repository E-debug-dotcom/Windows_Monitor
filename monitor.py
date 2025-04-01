import subprocess
import json
import re

def get_system_health():
    try:
        # Run PowerShell script
        result = subprocess.run(["powershell", "-File", "system_health.ps1"], capture_output=True, text=True)

        # Print raw output for debugging
        print("Raw Output:\n", result.stdout)

        # Extract only the JSON part using regex
        json_match = re.search(r"\{.*\}", result.stdout, re.DOTALL)

        if not json_match:
            print("Error: No valid JSON found in PowerShell output.")
            return None

        json_data = json_match.group(0)  # Extract JSON portion

        # Parse JSON
        data = json.loads(json_data)
        return data

    except json.JSONDecodeError as e:
        print(f"JSON Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    health_data = get_system_health()
    if health_data:
        print("\n📊 **System Health Report** 📊")
        print(json.dumps(health_data, indent=4))  # Pretty print JSON
