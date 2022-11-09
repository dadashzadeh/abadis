# abadis.ir
دریافت اطلاعات از سایت آبادیس

```html

Abadis().get_equivalent_persian_text('تست')
آزمایش|آزمون

Abadis().get_equivalent_persian_list(['تست', 'آزمایش'])
['آزمایش|آزمون', 'None']

Abadis().get_general_encyclopedia("تست")
['تست', 'تست (فیلم ۱۹۳۵)', 'تست (فیلم ۲۰۱۳)', 'تست (فیلم کوتاه)', 'تست (فیلم)']

Abadis().get_the_most_liked_comment("تست")
Test: سنجشTesting: سنجیدن
'''
