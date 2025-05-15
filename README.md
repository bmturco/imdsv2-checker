# IMDSv2 EC2 Compliance Checker

This Python script audits Amazon EC2 instances in a specified AWS region to determine whether **Instance Metadata Service v2 (IMDSv2)** is enforced.

---

## 🔍 Purpose

Enforcing IMDSv2 on EC2 instances is a recommended AWS security best practice to prevent SSRF (Server-Side Request Forgery) attacks and unauthorized metadata access. This script helps identify instances that are not compliant.

---

## 🧰 Features

- Lists all EC2 instances in a region
- Checks the `HttpTokens` setting in `MetadataOptions`
- Prints out:
  - Which instances are compliant (IMDSv2 enforced)
  - Which are non-compliant (IMDSv2 not enforced)
- Provides a summary report with instance IDs

---

## 🚀 Usage

### 1. **Prerequisites**
- Python 3.x
- `boto3` installed:
  ```bash
  pip install boto3
  ```
- AWS credentials must be configured (via `~/.aws/credentials`, environment variables, or IAM role)

### 2. **Run the Script**
```bash
python IMDSv2Check.py
```

By default, it checks the **`us-east-1`** region. To scan a different region, modify the script:
```python
check_imdsv2_status(region='us-west-2')
```

---

## 📦 Output

Example output:
```
[OK] i-xxxxxxxxxxxxxxxxx has IMDSv2 enforced.
[WARNING] i-xxxxxxxxxxxxxxxxx does NOT have IMDSv2 enforced.

Summary:
✔️ Compliant Instances: 1
❌ Non-Compliant Instances: 1
List of non-compliant instances:
 - i-xxxxxxxxxxxxxxxxx
```

---

## 📌 Notes

- This script uses the `describe_instances()` API, so IAM credentials need `ec2:DescribeInstances` permission.
- It only checks currently running/stopped instances in the specified region.

---

## 🔐 Security Recommendation

To enforce IMDSv2 on a non-compliant instance, you can use the AWS CLI:

```bash
aws ec2 modify-instance-metadata-options \
  --instance-id <instance-id> \
  --http-tokens required \
  --http-endpoint enabled
```

This will enable IMDSv2 enforcement without disabling metadata access.

---

## 📝 License

N/A

---

## 👤 Author

Script developed by Brenden Turco for internnal AWS security auditing purposes.
