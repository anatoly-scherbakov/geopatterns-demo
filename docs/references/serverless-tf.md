---
$id: https://serverless.tf
title: serverless.tf
author:
    $id: https://github.com/antonbabenko
    title: Anton Babenko
seeAlso: https://github.com/antonbabenko/serverless.tf
---

Набор модулей Terraform, предназначенных для упрощения развёртывания и управления ресурсами в облаке AWS. К нашей задаче больше всего подходит модуль [terraform-aws-lambda](https://github.com/terraform-aws-modules/terraform-aws-lambda), но мне не очевидно, что он действительно упрощает работу с ресурсами AWS Lambda. Это очень сложный модуль, и создаётся впечатление, что авторы пытаются превратить декларативный язык конфигурации Terraform в императивный. 

Представляется, что императивные задачи — такие, как сборка архива кода для публикации лямбда-функции — проще сделать на традиционном языке программирования, будь то Bash или Python.

Однако некоторые другие модули, скажем [terraform-aws-notify-slack](https://github.com/terraform-aws-modules/terraform-aws-notify-slack), весьма полезны даже на мой вкус. Этот последний собираюсь (на момент написания этого текста) втащить в наш рабочий проект.
