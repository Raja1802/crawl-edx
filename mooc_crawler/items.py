
import scrapy

class edxitem(scrapy.item):
    number = scrapy.field()
    key = scrapy.field()
    title = scrapy.field()
    short_description = scrapy.Field()
    full_description = scrapy.Field()
    level_type = scrapy.Field()
    marketing_url = scrapy.Field()
    enrollment_start = scrapy.Field()
    enrollment_end = scrapy.Field()
    end = scrapy.Field()
    start = scrapy.Field()
    org = scrapy.Field()
    length = scrapy.Field()
    effort = scrapy.Field()
    prerequisites = scrapy.Field()
    pacing_type = scrapy.Field()
    published = scrapy.Field()
    language = scrapy.Field()
    transcript_languages = scrapy.Field()
    availability = scrapy.Field()
    program_types = scrapy.Field()
    rating = scrapy.Field()
    review_count = scrapy.Field()
    instructor_1 = scrapy.Field()
    instructor_2 = scrapy.Field()
    instructor_3 = scrapy.Field()
    instructor_4 = scrapy.Field()
    instructor_5 = scrapy.Field()
    org_instructor_1 = scrapy.Field()
    org_instructor_2 = scrapy.Field()
    org_instructor_3 = scrapy.Field()
    org_instructor_4 = scrapy.Field()
    org_instructor_5 = scrapy.Field()
