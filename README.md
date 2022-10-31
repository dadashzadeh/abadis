# abadis.ir
دریافت اطلاعات از سایت آبادیس


print(Abadis().get_equivalent_persian_text('تست'))<br />
آزمایش|آزمون

print(Abadis().get_equivalent_persian_list(['تست', 'آزمایش']))<br />
['آزمایش|آزمون', 'None']

print(Abadis().get_general_encyclopedia("تست"))<br />
['تست', 'تست (فیلم ۱۹۳۵)', 'تست (فیلم ۲۰۱۳)', 'تست (فیلم کوتاه)', 'تست (فیلم)']

print(Abadis().get_the_most_liked_comment("تست"))<br />
Test: سنجشTesting: سنجیدن
