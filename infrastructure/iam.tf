resource aws_iam_role lambda {
  description        = "This role will grant the Lambda function with permissions it requires."
  assume_role_policy = data.aws_iam_policy_document.lambda.json
}


data aws_iam_policy_document lambda {
  statement {
    # Allow the Lambda function to assume this role, meaning - to act under it
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    effect = "Allow"
    sid    = ""
  }

  statement {
    # Allow the Lambda function to access files on our S3 bucket.
    effect = "Allow"
    actions = [
      # For simplicity, the Lambda function will have full access
      "s3:*"
    ]
    resources = [
      # The access is for the root directory of the bucket and for all of objects
      # in it.
      aws_s3_bucket.images.arn,
      "${aws_s3_bucket.images.arn}/*",
    ]
  }
}


resource aws_iam_role_policy_attachment basic {
  # Allow the Lambda function to write to Cloudwatch Logs.
  # We do not have to write that explicitly in the aws_iam_policy_document object
  # above because AWS has already prepared a nice re-usable policy we can just use.
  role      = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
