---
title: Бессерверные вычисления
template: presentation.html
---

<style>
@media print {
    hr { page-break-after: always; visibility: hidden; } /* page-break-after works, as well */
}

body {
    font-size: 28px;
}

h1 {
    text-align: center;
    font-size: 6rem;
}
</style>

# Introduction into Serverless Computing

Anatoly Scherbakov

Team Lead, Recall Masters Inc

---

# Хайп!!!111

<script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/2431_RC04/embed_loader.js"></script> <script type="text/javascript"> trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"serverless","geo":"","time":"today 5-y"}],"category":0,"property":""}, {"exploreQuery":"date=today%205-y&q=serverless","guestPath":"https://trends.google.com:443/trends/embed/"}); </script> 

---

# make deploy

```
aws_lambda_function.lambda: Still creating... [10s elapsed]
aws_lambda_function.lambda: Still creating... [20s elapsed]
aws_lambda_function.lambda: Still creating... [30s elapsed]
aws_lambda_function.lambda: Still creating... [40s elapsed]
aws_lambda_function.lambda: Still creating... [50s elapsed]
aws_lambda_function.lambda: Still creating... [1m0s elapsed]
aws_lambda_function.lambda: Still creating... [1m10s elapsed]
aws_lambda_function.lambda: Still creating... [1m20s elapsed]
aws_lambda_function.lambda: Still creating... [1m30s elapsed]
aws_lambda_function.lambda: Still creating... [1m40s elapsed]
aws_lambda_function.lambda: Still creating... [1m50s elapsed]
aws_lambda_function.lambda: Still creating... [2m0s elapsed]
aws_lambda_function.lambda: Still creating... [2m10s elapsed]
aws_lambda_function.lambda: Still creating... [2m20s elapsed]
aws_lambda_function.lambda: Still creating... [2m30s elapsed]
aws_lambda_function.lambda: Still creating... [2m40s elapsed]
aws_lambda_function.lambda: Creation complete after 2m48s [id=geopatterns-demo-api]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```
