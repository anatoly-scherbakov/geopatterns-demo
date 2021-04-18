locals {
  # You will have to change this variable to something else if you want to
  # deploy this project. Otherwise, your S3 bucket will clash with mine.
  project_name = "geopatterns-demo"
}


terraform {
  backend "s3" {
    region  = "us-east-1"
    encrypt = true

    # see tfstate.tf. We cannot use references here.
    bucket  = "geopatterns-demo-terraform-state"
    key     = "geopatterns-demo.tfstate"
  }
}
