resource "aws_iam_role" "lambda" {
  description        = "This role will allow Lambda function access to S3."
  assume_role_policy = data.aws_iam_policy_document.lambda.json
}


data "aws_iam_policy_document" "lambda" {
  # What AWS service can assume the IAM role?
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    effect = "Allow"
    sid    = ""
  }
}
