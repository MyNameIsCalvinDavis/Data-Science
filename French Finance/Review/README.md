
# Review

In this document, I try to reflect and understand, informally, the quality of my report and what I can do to improve it in the future. Mostly this is for my own reflection, so it’s not formatted in a reportable format. 

## Challenges

The biggest challenge that this competition presented was obtaining a contextual, business understanding of the data. With over 1000 columns, many of them empty, within a context (french taxes) I’m not familiar with, from a dubious data source, with arbitrary analysis goals, there was a lot to parse through with this competition.

Usually the datasets I work on are pretty straightforward and unambiguous. Generally there are two types of data I tend to work on:

* Raw sensor data. This comes from usually hardware sensors, and contains many extraneous fields that aren’t necessarily relevant to the data analysis. Often it’s easy to pare down this data to a smaller subset of columns and work with them directly. Most of the columns are easily contextualized, and often establishing a composite primary key between disparate data sets is easy because they have internal selectors already, like ZIP code, city name, <ID>, or some other unique tag. At the very least, these primary keys are usually translatable to other primary keys in a different dataset.

* Relational data. Shares many of the same traits as sensor data, with the added benefit that I can usually always identify a composite primary key with ease.

There are other types of data too like geospatial data, like what the census bureau uses, or any sort of GIS data, though they have their own problems.

Regardless, none of the data I work with tends to lack context. Seldom do I receive a dataset that is ambiguously defined and requires intense organizational understanding to digest mentally, which is exactly what this dataset was. As a random american living in Texas, I had a very poor understanding of the French fiscal tax system, so analyzing said system was a deeper research project than just loading it all into pandas and shooting from the hip.

### Specific Challenges

* Researching French Taxes
* Organizing the report
* Organizing the code
* Data analytics
* Time management with all of the above

Understandably, these are all related to each other, and I did a poor job and intermingling them effectively. Let’s talk about why.

### Researching French Taxes

This is the easiest one to write about… I’m not a French G-man, so I didn’t know what I was doing. That’s basically it. Moving through 1000 columns that are all written in french, with french acronyms, was a difficult task. In the real world I’d consult with a SME on what fields might yield the best results, or be the most relevant, or understand how certain subsets of columns interacted with one another.

For the most part, I think I did fine here. I went through each column and identified a pattern of terminology (outlined in the report, I won’t go over it here) and then used those columns to inform my analytics. Not too different than what everyone else submitted.

### Organizing the Report

Bigger issue – when I do analytics, often times I tackle the data first without having a broader understanding or plan, and rely upon “The Process(tm)” to reveal further insights about the data. What I mean is, I will load up a dataset and begin applying aggregate functions, normalizations, regressions, etc, without a real plan. So my understanding of the data evolves over time, instead of spending a lot of time doing this at the beginning.

So when writing the report… what am I writing exactly? How do I organize it? What goes first, what goes last, what does the customer actually care about? The hardest part of this project was: They have no idea. Neither do I. And focusing my effort on report-able items, supported by code, was backwards from how I usually do things which is write code, and then report on my findings.

#### Need

In the future I need to take a more critical look at the data and determine what types of things I can take from it, and either before or after, format a report outline. Probably in conjunction. One difficulty is that without a granular understanding of the data (done through code), it’s hard to make these conclusions. So probably making a general outline (broad aggregations, broad regressions, etc) and then as the data presents more and more information, add sub-categories and work on answering them and any obvious derivatives explicitly.

Part of that is also a section about the data. Data about data. Metadata, even. Column names, sizes, types, unique values, value counts, etc, used to inform me about decisions I could make moving forward into the report.

### Organizing the Code

I often ran into the following conundrum: Do I make my notebook look pretty, or do I make the report look pretty? Is my notebook the report? If not, do I still need to organize my notebook? How much?

The computer-sciencey problem I ran into (clean code anyone?) was that I did not do nearly enough abstraction or functional analysis of the things I was doing. Mostly because my biggest constraint was dev time, not efficiency, speed, or maintainability. Often the opposite is true, so this was a weird turn for me.

I don’t know how important writing ubiquitous functions are in a project like this, because in these types of problems, usually the application of some <process> or <algorithm> is sufficiently different that it bears doing individually, even if it’s 90% similar as something else. Could I engineer that 90% solution? Sure – and I’ve even tried. But then when the next problem set is only 85% similar, I have to re-engineer all of my other solutions to make them fit the monolith function. Not worth it. Very satisfying, but not worth it.

#### Need

Ultimately I need to tie my code to specific objectives defined in my report outline, and organize them as such in my notebook, but not in a presentable way. I don’t need my notebook to be presentable unless it’s my deliverable. I also need to spend some time normalizing my data before I do any analysis, which I didn’t do so much in this challenge.

As for functionality… I don’t know how much I care. Normalization at the beginning of a notebook should take care of it.

### Data Analytics

This is a funny one – I am a data scientist, not a data analyst. When viewing other submissions, I saw both! Crazy! Actual insights into the data and conclusions / extrapolations about what the data could mean. Assumptions. Reflections. Technically data driven, but not data. I thought that was interesting… it showed that I really only did half of the challenge – I did a data science report, not a data analytics report, I did not infer or conclude anything necessarily, I just showed what WAS. Just how things were, what the data was. No analytics, no reflection. Oops.

That’s not something I particularly enjoy, but it’s necessary for a project like this.

#### Time Management

Yeah this one hits hard, and part of the reason is because my attack was largely disorganized. I just started writing code and expected a report to magically pop out of it, and was surprised when that didn’t happen. Between organizing the report and my code, and the actual research portion of this project, these factors compounded into a total mess of time management that easily doubled my time commitment to this project. With any advance planning at all of how my report might look, this wouldn’t have been as big of an issue, and won’t be an issue moving forward.
