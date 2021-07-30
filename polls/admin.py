from django.contrib import admin

# must import these all
from .models import choice, question,was_published_recently

# stacks
# class ChoiceInline(admin.StackedInline):
#     model = choice
#     extra = 3

# the same as the above, difference is its in the same line, unlike the 1st 1, stacked
class ChoiceInline(admin.TabularInline):
	model = choice
	extra = 3

# Question format
class QuestionAdmin(admin.ModelAdmin):
	# The Date Information can hide/show in admin site because of the ['collapse']
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]

	# shows and allows you to add choices while doing the question
	inlines = [ChoiceInline]

	# To view each question w/ its details after clicking the 'Questions' in sidebar
	list_display = ('question_text', 'pub_date', was_published_recently)

	# for filter sidebar via pub_date
	list_filter = ['pub_date']

	# allows you to search
	search_fields = ['question_text']

admin.site.register(question, QuestionAdmin)