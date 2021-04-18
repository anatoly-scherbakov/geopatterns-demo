resource "aws_s3_bucket" "tfstate" {
  # Bucket to store the Terraform state file.
  bucket = "${local.project_name}-terraform-state"

  versioning {
    enabled = true
  }
}
