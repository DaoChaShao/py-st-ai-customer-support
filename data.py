#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/10 12:02
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   data.py
# @Desc     :   

CUSTOMER_QUESTION: list[str] = [
    "这个有官方授权吗？",  # “这个商品是正品吗？”
]

CUSTOMER_QUESTIONS: list[str] = [
    "什么时候能发货？",
    "快递单号是多少？",
    "可以退货吗？",
    "我怎么申请退款？",
    "有没有优惠券？",
    "尺码怎么选？",
    "这件衣服有现货吗？",
    "这个商品是正品吗？",
    "可以发顺丰吗？",
    "我付完款了，怎么还没发货？"
]

INTENTS_CATEGORIES: dict[str, list[str]] = {
    "商品咨询": ["这件衣服有现货吗？", "还有其他颜色吗？"],
    "售后服务": ["我可以退货吗？", "怎么申请退款？"],
    "物流查询": ["快递到了吗？", "怎么查物流？"],
    "促销优惠": ["有优惠吗？", "有没有满减活动？"]
}

INTENTS_QUESTIONS: list[str] = [
    "这件衣服有现货吗？",
    "还有其他颜色吗？",
    "我可以退货吗？",
    "怎么申请退款？",
    "快递到了吗？",
    "怎么查物流？",
    "有优惠吗？",
    "有没有满减活动？",
]

PERSONALISED_QUESTIONS: list[str] = [
    "这产品适合我这个年龄使用吗？",
    "有没有适合我这种级别的其他产品？",
    "你们有推荐搭配的配件吗？",
    "这个产品我是第一次买，有没有什么建议？",
    "我比较容易过敏，这个产品适合我吗？",
    "有没有适合我这个年龄的其他产品？",
    "有适合我这个性别的其他颜色推荐吗？",
]
