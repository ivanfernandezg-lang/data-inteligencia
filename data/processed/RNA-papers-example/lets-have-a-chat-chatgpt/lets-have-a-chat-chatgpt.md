# Lets have a Chat ChatGPT

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Let’s have a chat! A Conversation with ChatGPT: Technology, 
Applications, and Limitations 
Sakib Shahriar 1*, Kadhim Hayawi² 
School of Computer Science, University of Guelph, Guelph, Ontario, Canada¹ 
College of Interdisciplinary Studies, Computational Systems, Zayed University, Abu Dhabi, UAE² 
 
Abstract 
The emergence of an AI-powered chatbot that can generate human-like sentences and write coherent essays 
has caught the world's attention. This paper discusses the historical overview of chatbots and the technology 
behind Chat Generative Pre-trained Transformer, better known as ChatGPT. Moreover, potential 
applications of ChatGPT in various domains, including healthcare, education, and research, are highlighted. 
Despite promising results, there are several privacy and ethical concerns surrounding ChatGPT. In addition, 
we highlight some of the important limitations of the current version of ChatGPT. We also ask ChatGPT 
to provide its point of view and present its responses to several questions we attempt to answer. 
Keywords: Artificial intelligence; Natural Language Processing; ChatGPT; Text Generation; Chatbots 
 
 
 
 
 
1. Introduction 
In 1950, the British computer scientist Alan Turing disputed whether human reasoning can be matched 
by computers: “Can machines think?” [1]. Subsequently, he proposed the Turing Test to measure computer 
or artificial intelligence. In a Turing test, a human interrogator is presented with responses from a human 
and a computer (with the ability to generate written texts in real-time). If the interrogator cannot distinguish 
between the answers, the computer system passes the Turing Test. Although several computer programs 
and chatbots like Eliza demonstrated success in the Turing test ([2] [3]), these programs arguably used 
certain tricks to pass the test [4] rather than demonstrating any significant intelligence. With the 
advancement in machine learning and natural language processing (NLP), chatbots have gained significant 
research attention and have been used for a variety of commercial and non-commercial applications ([5], 
[6], [7], [8], [9]). Despite their vast adoption, most chatbots do not have personalization, and user 
 
* This is to indicate the corresponding author. 
 Email address: shahrias@uoguelph.ca

---

## Página 2

satisfaction remains questionable [10]. This limitation prompted researchers and developers to focus on 
chatbot engagement in making chatbots more conversational. 
In November 2022, OpenAI released a novel AI-powered chatbot called ChatGPT2, which gained 
significant public attention. Unlike any previous chatbots, ChatGPT has surprised the public with its 
coherent responses to various questions. In this short paper, we explore the technology enabling the success 
of ChatGPT and highlight several domains and applications of ChatGPT. We also invited ChatGPT to 
respond to some of the questions we attempted to answer, starting with its response to the history of 
chatbots. 
  
Question: Hi ChatGPT, tell us about the history of chatbots 
ChatGPT: Certainly! The idea of a machine that could simulate human conversation dates back several 
decades. In fact, the first chatbot was created in the 1960s by MIT computer scientist Joseph Weizenbaum. 
Weizenbaum's chatbot, called ELIZA, used a set of rules to simulate conversation by asking questions and 
giving scripted responses. ELIZA was designed to imitate a psychotherapist, and people were often 
surprised at how convincingly it could simulate human conversation. 
Over the years, chatbots have continued to evolve and improve. One of the key advancements was the 
development of natural language processing (NLP) technology, which allows chatbots to understand and 
respond to human language more accurately. In the 1990s and early 2000s, chatbots began to be used for 
customer service and support, with companies like AOL and Microsoft developing chatbots to help users 
with their software and services. 
In recent years, there has been a surge of interest in chatbots, driven in part by advancements in artificial 
intelligence and machine learning. Modern chatbots use a combination of NLP, machine learning, and 
other AI technologies to understand and respond to human language in a more natural and nuanced way. 
They are now used in a wide range of applications, from customer service and support to personal 
assistants and entertainment. 
Overall, the history of chatbots is a fascinating one that reflects the evolution of AI and our growing 
desire to create machines that can understand and interact with us in more human-like ways. 
 
Our first observation is that the response from ChatGPT appears to be very coherent, engaging, and free 
of grammatical errors. We also notice that ChatGPT does well in providing factual information. It manages 
to cite names and dates accurately. Interestingly, ChatGPT does not talk about itself, and we understand 
that it is limited in presenting information after September 20213. Finally, it is also captivating to observe 
that ChatGPT has ended its response with a summary offering its viewpoint. 
 
2 https://openai.com/blog/chatgpt/ 
3 
https://www.forbes.com/sites/ariannajohnson/2022/12/07/heres-what-to-know-about-openais-chatgpt-what-its-
disrupting-and-how-to-use-it/?sh=41280f462643

---

## Página 3

2. ChatGPT Technology: From Language Models to Reinforcement Learning 
Machine learning, a subfield of artificial intelligence (AI), is defined as the ability of computer systems 
to learn from experience without being explicitly taught or programmed. With advances in computing 
power, increasing data availability, and algorithmic improvements, deep learning has emerged as a high-
performing predictive tool. Unlike traditional machine learning, deep learning algorithms use artificial 
neural networks, often in a large capacity. Deep learning models generally require more training data but 
can provide better generalization. Transformers or large language models are a special family of deep 
learning models that have emerged as state-of-the-art solutions for text data. From text classification to text 
generation, these models offer superior performance than other AI models. Language models are usually 
pre-trained on large language corpus, such as Wikipedia, but can be fine-tuned for a specific task. The two 
most prominent language models include Bidirectional Encoder Representations from Transformers 
(BERT) [11] and Generative Pretrained Transformer (GPT) [12]. The former is primarily used for 
recognizing the context in language and classification tasks, while the latter is more adept at language 
generation tasks such as machine translation and question-answering. 
Several chatbots prior to ChatGPT used language models. However, the main component that allowed 
ChatGPT its coherent and engaging responses is attributed to the use of reinforcement learning. In this 
context, human evaluators ranked the responses of ChatGPT, which allowed it to optimize some of its 
parameter to essentially become a better conversationalist. ChatGPT was developed on top of GPT-3, a 
generative autoregressive language model with 175 billion parameters [13]. To train such a complex 
network, OpenAI partnered with Microsoft with a reported training resource of over 350GB of memory 
costing $12 million4. 
 
Question: Hi ChatGPT, how were you were developed? 
ChatGPT: Hello! I was developed by OpenAI, a research organization focused on advancing artificial 
intelligence in a safe and beneficial way. Specifically, I was developed by a team of researchers and 
engineers at OpenAI who used a deep learning technique called a transformer to train me on a large corpus 
of text data. The transformer is a type of neural network that is especially good at processing sequential 
data, like language. 
To train me, the team fed me huge amounts of text from a variety of sources, including books, articles, 
and websites. They then used a process called unsupervised learning to teach me to recognize patterns in 
the text data. Through this process, I learned to understand and generate natural language. 
After my initial development, I went through a rigorous testing and refinement process to ensure that I 
was accurate, reliable, and safe to use. And since my release, I have been continually updated and improved 
to better serve my users. 
 
 
4 https://venturebeat.com/ai/ai-machine-learning-openai-gpt-3-size-isnt-everything/

---

## Página 4

Like the first answer, we were impressed with the engaging nature and structure of the response from 
ChatGPT. We noticed that ChatGPT mentions the use of unsupervised learning for recognizing patterns, 
which is accurate and was outlined in the GPT paper [12]. Another interesting observation is that ChatGPT 
describes the final phase as a ‘testing and refinement process’ without mentioning reinforcement learning 
or additional details. 
3. Applications of ChatGPT 
Despite being released to the public domain very recently, ChatGPT has already gained significant 
research attention. In this section, we describe recent works investigating the use of ChatGPT for various 
research and applications. Thorp [14] provided a qualitative assessment of ChatGPT responses to research 
topics, such as education, literature, and scientific writing. ChatGPT provided an entertaining writeup when 
asked to complete a scene from a classic play. In terms of education, ChatGPT can provide factual answers 
but still has some way to go in writing essays. In another study [15], researchers were asked to distinguish 
between abstracts of scientific papers written by ChatGPT and humans. The results are surprising as human 
evaluators only identified 68% of the abstracts to be generated by ChatGPT. De Angelis et al. [16] discussed 
the evaluation of language models in light of ChatGPT and highlighted potential ethical and practical 
challenges in medicine and public health. The main challenges include the potential of AI-driven 
misinformation or “infodemic” that is often difficult to discern. 
In the field of medicine and public health, ChatGPT has already been explored for various applications. 
Khan et al. [17] discussed several potential applications of ChatGPT in medical education, including 
personalized learning and generating case studies. The authors also pointed out that ChatGPT can be used 
in clinical management for documentation and decision support. Rao et al. [18] evaluated the effectiveness 
of ChatGPT in providing clinical decision support in radiology. The authors provided ChatGPT with text 
prompts such as “For variant ‘Breast cancer screening. Average-risk women: women with <15% lifetime 
risk of breast cancer.’, determine the single most appropriate imaging procedure” to evaluate its efficacy in 
breast cancer screening and breast pain detection. ChatGPT performed relatively well for the former task 
with 88.9% correct responses but only managed 58.3% correct responses for breast pain. The role of 
ChatGPT and generative AI in helping urologists has also been discussed [19]. ChatGPT can primarily help 
urologists in low-complexity tasks, giving them more time to focus on patients. Hulman et al. [20] utilized 
ChatGPT to answer frequently asked questions about diabetes and asked healthcare employees to 
distinguish between human and ChatGPT-generated answers. The authors found that the evaluators could 
identify answers generated by ChatGPT correctly 59.5% of the time. The authors also concluded that 
despite ChatGPT not being trained exclusively in medical data, it has clinical knowledge and can identify 
information about disease management. Generating a medical report about a given topic may be useful in 
pharmaceutical education. To this end, Zhu et al. [21] prompted ChatGPT to generate a mini-review on 
“lipid-based drug delivery systems.” The authors concluded that ChatGPT can structure the topic well with 
meaningful conclusions for the readers. However, there are question marks over the accuracy due to a lack

---

## Página 5

of reliable citations. Shen et al. [22] summarized other potential use cases and implications for ChatGPT in 
medicine. 
Researchers also investigated whether ChatGPT can answer medical exam questions. Kung et al. [23] 
tested the performance of ChatGPT on the US medical licensing exam, consisting of three standardized 
tests required for medical licensure in the US. ChatGPT performed at the passing threshold level with 60% 
accuracy without specialized input from humans. Any questions containing visual information, such as 
medial images, were removed. The results demonstrate the potential of ChatGPT for medical education and 
assistance in clinical-decision making. However, in a Chinese national medical licensing exam, ChatGPT 
performed considerably lower, with 45.8% correct answers [24]. In Ophthalmology, ChatGPT was tested 
with questions from the Ophthalmic knowledge assessment program containing two exams and obtained 
55.8% and 42.7% accuracy, respectively [25]. For a basic and advanced cardiovascular life support exam 
from the American Heart Association, ChatGPT performed below the 84% passing threshold [26]. 
However, its ability to provide detailed rationality with reasonable accuracy makes it a potentially useful 
tool for self-learning and exam preparation. Mbakwe et al. [27] argued that the success of ChatGPT in 
answering medical examinations boils down to the nature of these exams being rote memorization rather 
than testing analysis and critical thinking. 
One of the significantly anticipated applications of chatbots is in the domain of education. AI and 
technology can be effective in education in several aspects, including personalized learning [28]. In this 
context, ChatGPT can enhance student participation, provide experiential learning, and help educators in 
the evaluation of exams and content preparation [29]. Several researchers focused their studies on the 
impact of ChatGPT in education ([30], [31], [32], [29]). Potential concerns of ChatGPT in education include 
response bias ([31] [32]), cheating [30], leakage of private data ([31] [32]), and transparency [32]). Chatbots 
can also contribute effectively to peer tutoring. Pardos and Bhandari [33] found that 70% of the hints offered 
by ChatGPT in elementary and intermediate Algebra topics could result in positive learning gains for 
students. Frieder et al. [34] evaluated the mathematical capabilities of ChatGPT in helping Mathematicians 
with tasks like question answering and finding theorems. The researchers found that ChatGPT displayed a 
level of Mathematics proficiency below those of an average graduate student. There is public concern about 
ChatGPT being used for plagiarism, and it is necessary to create tools to detect such plagiarism. To this 
end, Khalil and Er [35] attempted to utilize ChatGPT as a plagiarism detection tool and found that responses 
created by ChatGPT can often go undetected by other plagiarism checkers. Meanwhile, when ChatGPT 
was asked to check if the writing was generated by itself, it performed better than other plagiarism detection 
software. Yang et al. [36] explored ChatGPT’s ability in summarizing written texts and found that ChatGPT 
performs on par with existing fine-tuning methods based on Rouge scores. The authors also highlighted 
that the current maximum input token length of 5000 is a limitation in assessing ChatGPT’s ability in text 
summarizing. Can ChatGPT improve student essays? To answer this question, Basic et al. [37] conducted 
a study with nine students in the control group and nine in the experimental group that used ChatGPT. The 
authors concluded that ChatGPT does not necessarily improve essay quality because the control group 
outperformed the experimental group in most criteria.

---

## Página 6

Bang et al. [38] evaluated the effectiveness of ChatGPT on ten reasoning tasks, such as logical reasoning 
and commonsense reasoning. The authors found that ChatGPT performs reasonably well on deductive 
reasoning tasks but extremely poor on inductive reasoning. ChatGPT also does well on commonsense 
reasoning. For instance, ChatGPT was asked the following question; Please judge if this predicate is (likely) 
plausible or implausible: “knife chop rock.” To which it answered: It is implausible that a knife could chop 
through a rock. Knives are made to cut through softer materials such as food, paper, or wood. Rocks are 
much harder than these materials and a knife would not be able to make a dent in a rock, let alone chop it. 
ChatGPT remains a potentially beneficial tool in journalism and misinformation detection, particularly 
for references and fact-checking. During the COVID-19 pandemic, vaccine misinformation led to vaccine 
hesitancy in social media [39]. Sallam et al. [40] provide a descriptive analysis of ChatGPT’s response to 
vaccine conspiracy statements and compulsory vaccination. The study found that ChatGPT was dismissive 
of conspiracy statements but provided divided opinions for vaccine mandates by highlighting  the pros and 
cons.  
In software development, ChatGPT can be used for tutoring and software testing. Jalil et al. [41] 
evaluated ChatGPT’s capabilities in software testing by presenting it with textbook questions. The results 
are not promising in this case as ChatGPT managed to answer correctly only 37.5% of the answers. Jiao et 
al. [42] evaluated ChatGPT’s performance in translation on several benchmark sets. In high-resource 
European languages, ChatGPT performs on par with commercial applications like Google Translate. 
However, for low-resource or distant languages, the performance is significantly worse. At this point, let 
us ask ChatGPT about its potential use in various domains. 
 
Question: Hi ChatGPT, in what ways can you be used in healthcare, education, and research? 
ChatGPT: Hi! As an AI language model, I can be used in various ways in healthcare, education, and 
research. Here are some examples: 
 
In Healthcare: 
1) Medical Diagnosis and Treatment: AI language models can be trained to analyze medical data such as 
medical images, electronic health records, and other patient information to assist in medical diagnosis and 
treatment. This can help healthcare professionals make more accurate and informed decisions regarding 
patient care. 
2) Patient Interaction: AI language models can be used to help patients interact with healthcare providers 
and provide them with information about their health conditions, treatment options, and medication 
instructions. 
3) Medical Research: AI language models can help researchers process and analyze large volumes of 
medical data and identify patterns and trends in disease outbreaks, drug efficacy, and patient outcomes. 
 
In Education: 
1) Language Learning: AI language models can help language learners improve their language proficiency 
by providing them with personalized feedback, practice exercises, and conversation simulations.

---

## Página 7

2) Educational Content Creation: AI language models can be used to generate educational content such as 
quizzes, flashcards, and study guides that are customized to meet the needs of individual learners. 
3) Academic Research: AI language models can be used to analyze academic texts and generate summaries, 
insights, and recommendations that can help researchers gain new insights and discoveries. 
 
In Research: 
1) Data Analysis: AI language models can be used to analyze large volumes of data from various sources 
and identify patterns, trends, and correlations that are not easily visible to human researchers. 
2) Text Mining: AI language models can help researchers extract relevant information from large volumes 
of unstructured text data such as research papers, news articles, and social media posts. 
3) Research Collaboration: AI language models can help researchers collaborate with each other by 
providing real-time translation services, automated proofreading and editing, and content summarization. 
 
Question: What about journalism and software development? 
ChatGPT: Certainly! As an AI language model, I can also be used in journalism and software development 
in several ways: 
 
In Journalism: 
1) News Writing and Summarization: AI language models can be used to generate news articles and 
summaries automatically, saving time and resources for journalists and news organizations. 
2) Fact-Checking: AI language models can help fact-check news stories and verify the accuracy of the 
information presented. 
3) Personalization: AI language models can help personalize news content for individual readers based on 
their interests, reading history, and location. 
 
In Software Development: 
1) Chatbots: AI language models can be used to power chatbots, which can interact with users and answer 
their questions in natural language. 
2) Code Generation: AI language models can be used to generate code automatically, reducing the time 
and effort required for software development. 
3) Bug Detection: AI language models can be used to detect bugs and errors in code, improving the quality 
and reliability of software applications. 
 
Question: In what other domains can you be used for? 
ChatGPT: As an AI language model, I can be used in a wide range of domains beyond healthcare, 
education, research, journalism, and software development. Here are a few examples: 
 
1) Customer Service: AI language models can be used to power chatbots and virtual assistants that can 
provide customer service and support to users.

---

## Página 8

2) Financial Services: AI language models can be used to analyze financial data and detect fraud, as well 
as provide personalized financial advice to individuals. 
3) Marketing and Advertising: AI language models can help marketers generate ad copy and content, 
analyze customer sentiment and behavior, and personalize marketing campaigns for individual users. 
4) Legal Services: AI language models can be used to analyze legal documents and provide legal advice to 
individuals and businesses. 
5) Social Media: AI language models can be used to analyze social media content, monitor online 
conversations, and detect patterns and trends in user behavior. 
6) Gaming: AI language models can be used to generate dialogue and narrative content for video games, 
as well as power virtual assistants and chatbots within games. 
7) Transportation: AI language models can be used to power voice assistants in vehicles and help drivers 
navigate and control various vehicle systems. 
8) Robotics: AI language models can be used to enable natural language interaction between humans and 
robots, as well as help robots understand and respond to human commands and requests. 
These are just a few examples of how AI language models like me can be used in various domains. The 
possibilities are endless, and new applications are being developed every day as AI technology advances. 
 
ChatGPT has raised a lot of eyebrows for its potential use in writing scientific articles. According to 
Stokel-Walker [43], four papers have listed ChatGPT as a co-author for its writing contributions. However, 
leading publishers like Science have dismissed the possibility of listing an AI chatbot as a co-author while 
other publishers, including Taylor & Francis, are reviewing their policy when it comes to this issue. Several 
journals, including the Korean Journal of Radiology, have published policies rejecting any contributions as 
co-authors from ChatGPT or other AI models [44]. On the other hand, other journals published guidelines 
recommending the acknowledgment of any AI tools used for the research but do not allow them to be listed 
as co-authors ([45], [46]). Researchers have also called on journals to clarify what proportion of their papers 
contain AI-generated content [47] and publish guidelines for AI use in writing papers [48]. Korinek [49] 
explored the potential use cases of language models like ChatGPT for Economic research. The author 
argues that researchers can be more productive by using language models for tasks like editing and 
generating headlines. Chen [50] discussed some of the ethical concerns and potential benefits of using AI 
tools for scientific writing. The author argued that chatbots can assist writers whose native language is not 
English. The paper was written by the author in Chinese and summarized by ChatGPT and translated to 
English by AI tools. Aydın and Karaarslan [51] utilized ChatGPT to write a literature review on the role of 
Digital twins in healthcare. Despite the promising results, the authors found that ChatGPT had significant 
matches on a plagiarism checker when paraphrasing sentences. Dowling and Lucey [52] found that 
ChatGPT is effective in generating plausible research ideas, literature reviews, and testing frameworks. 
They also noted that the research quality improves significantly when domain expertise is added as input. 
Although ChatGPT can potentially speed up research and writing of scientific papers, there should be 
human oversight and fact-checking as language models like ChatGPT may generate misleading information 
([53], [54], [55], [56]). Table 1 summarizes the existing works utilizing ChatGPT in several domains.

---

## Página 9

Table 1 Applications of ChatGPT in Existing Works 
Domain 
Application 
Method 
Results 
Medicine and Public Health 
Clinical decision support in 
radiology [18] 
Provided text prompts and 
evaluated diagnosis response 
for breast cancer screening 
Effective in breast cancer 
screening but not in breast 
pain detection 
Improving 
efficiency 
in 
Urology [19] 
Discussed 
the 
role 
of 
generative AI in helping 
urologists 
N/A 
Answer 
frequently 
asked 
medical questions [20] 
Asked human evaluators to 
distinguish between ChatGPT 
and 
human 
answers 
to 
diabetes-related questions 
The evaluators could only 
identify 
answers 
to 
be 
generated by ChatGPT 59.5% 
of the time 
Write a short review on a 
medical topic [21] 
ChatGPT was asked to write a 
mini review on lipid-based 
drug delivery systems 
ChatGPT can benefit readers 
with general knowledge but 
the accuracy of analysis is 
questionable due a lack of 
reliable citations 
Take on medical exam [23] 
Asked ChatGPT questions 
from US medical licensing 
exam 
after 
removing 
questions 
with 
visual 
information 
ChatGPT performed near the 
passing threshold of 60% 
accuracy 
Take on a medical exam in 
Chinese [24] 
Asked ChatGPT questions 
from the Chinese national 
medical licensing exam 
ChatGPT 
performed 
considerably 
lower, 
with 
45.8% correct answers  
Take 
on 
Ophthalmology 
exam [25] 
Asked ChatGPT questions 
from Ophthalmic knowledge 
assessment program 
Obtained 55.8% and 42.7% 
accuracy on the two exams, 
respectively 
Take on a life support exam 
[26] 
Asked ChatGPT questions 
from basic and advanced 
cardiovascular life support 
exams by the American Heart 
Association 
Despite scoring below the 
passing threshold, ChatGPT 
showed promising results by 
providing 
detailed 
explanation of its rationale 
Education 
Analyze impact of ChatGPT 
in education ([30], [31], [32]) 
Highlighted potential benefits 
and ethical concerns 
N/A 
Algebra tutoring [33] 
Used ChatGPT to generate 
hints for Algebra topics 
70% of the hints could result 
in positive learning gains for 
students 
Assess 
Mathematics 
proficiency of ChatGPT [34]  
Created a dataset containing 
questions 
related 
to 
elementary 
arithmetic 
problems, 
symbolic 
problems, and other exercises 
For most problems, ChatGPT 
does not cross the passing 
threshold 
Plagiarism Detection Tool 
[35] 
Asked ChatGPT to determine 
if a writing was generated by 
itself 
Performed better than other 
plagiarism detection software

### Tabla 1 (Página 9)

| Domain | Application | Method | Results |
| --- | --- | --- | --- |
| Medicine and Public Health | Clinical decision support in
radiology [18] | Provided text prompts and
evaluated diagnosis response
for breast cancer screening | Effective in breast cancer
screening but not in breast
pain detection |
|  | Improving efficiency in
Urology [19] | Discussed the role of
generative AI in helping
urologists | N/A |
|  | Answer frequently asked
medical questions [20] | Asked human evaluators to
distinguish between ChatGPT
and human answers to
diabetes-related questions | The evaluators could only
identify answers to be
generated by ChatGPT 59.5%
of the time |
|  | Write a short review on a
medical topic [21] | ChatGPT was asked to write a
mini review on lipid-based
drug delivery systems | ChatGPT can benefit readers
with general knowledge but
the accuracy of analysis is
questionable due a lack of
reliable citations |
|  | Take on medical exam [23] | Asked ChatGPT questions
from US medical licensing
exam after removing
questions with visual
information | ChatGPT performed near the
passing threshold of 60%
accuracy |
|  | Take on a medical exam in
Chinese [24] | Asked ChatGPT questions
from the Chinese national
medical licensing exam | ChatGPT performed
considerably lower, with
45.8% correct answers |
|  | Take on Ophthalmology
exam [25] | Asked ChatGPT questions
from Ophthalmic knowledge
assessment program | Obtained 55.8% and 42.7%
accuracy on the two exams,
respectively |
|  | Take on a life support exam
[26] | Asked ChatGPT questions
from basic and advanced
cardiovascular life support
exams by the American Heart
Association | Despite scoring below the
passing threshold, ChatGPT
showed promising results by
providing detailed
explanation of its rationale |
| Education | Analyze impact of ChatGPT
in education ([30], [31], [32]) | Highlighted potential benefits
and ethical concerns | N/A |
|  | Algebra tutoring [33] | Used ChatGPT to generate
hints for Algebra topics | 70% of the hints could result
in positive learning gains for
students |
|  | Assess Mathematics
proficiency of ChatGPT [34] | Created a dataset containing
questions related to
elementary arithmetic
problems, symbolic
problems, and other exercises | For most problems, ChatGPT
does not cross the passing
threshold |
|  | Plagiarism Detection Tool
[35] | Asked ChatGPT to determine
if a writing was generated by
itself | Performed better than other
plagiarism detection software |

---

## Página 10

Text Summarization [36] 
Compared 
ChatGPT’s 
performance in summarizing 
texts with other fine-tuning 
models 
Similar 
performance 
to 
existing models in terms of 
Rouge scores 
Improve essay quality [37] 
Divided students into control 
and 
experimental 
groups 
(who 
used 
ChatGPT) 
to 
assess their essays 
No evidence of ChatGPT 
improving writing quality as 
control group outperformed 
experimental group 
Reasoning 
Evaluate ChatGPT on various 
reasoning tasks [38] 
Proposed 
framework 
to 
evaluate 
the 
multitask, 
multilingual, and multimodal 
reasoning of language models 
Performs well on deductive 
and commonsense reasoning 
but not on inductive reasoning 
Journalism 
and 
Misinformation Detection 
Evaluate ChatGPT response 
on conspiracy statements and 
politically divided ideas [40] 
Performed a descriptive study 
on ChatGPT responses to 
various COVID-19 vaccine 
topics 
ChatGPT was dismissive of 
conspiracy 
statements 
but 
remained 
neutral 
on 
controversial political views 
by stating pros and cons 
Software Development 
Evaluate ChatGPT’s response 
to software testing questions 
[41]  
Asked ChatGPT to respond to 
textbook 
questions 
in 
a 
common 
software 
testing 
curriculum  
Only 37.5% of the questions 
were correctly answered 
Translation 
Evaluate ChatGPT’s ability in 
translation [42] 
Used several benchmark test 
sets to compare ChatGPT’s 
responses in translating 
Performs 
on 
par 
with 
commercial applications for 
high-resource 
European 
languages but lags behind on 
distant languages 
Scientific Research 
Write scientific and academic 
papers [43] 
Discussed several papers who 
used and listed ChatGPT as 
authors 
Highlighted potential ethical 
concerns 
Automation 
in 
Economic 
research [49] 
Highlighted use cases of 
ChatGPT 
in 
research, 
including language editing 
and headline generation 
N/A 
Summarize 
and 
translate 
research papers for non-
native English speakers [50] 
Used ChatGPT to summarize 
and other AI tools to translate 
Chinese written paper 
Coherent writing style after 
manual screening. Potential 
benefit 
in 
speeding 
up 
research 
but 
has 
several 
ethical concerns 
 
4. Limitations of ChatGPT 
ChatGPT certainly has the potential for diverse and interesting applications. However, users should 
consider the limitations of the current model. In this section, we outline some of the current limitations of 
ChatGPT.

### Tabla 1 (Página 10)

|  | Text Summarization [36] | Compared ChatGPT’s
performance in summarizing
texts with other fine-tuning
models | Similar performance to
existing models in terms of
Rouge scores |
| --- | --- | --- | --- |
|  | Improve essay quality [37] | Divided students into control
and experimental groups
(who used ChatGPT) to
assess their essays | No evidence of ChatGPT
improving writing quality as
control group outperformed
experimental group |
| Reasoning | Evaluate ChatGPT on various
reasoning tasks [38] | Proposed framework to
evaluate the multitask,
multilingual, and multimodal
reasoning of language models | Performs well on deductive
and commonsense reasoning
but not on inductive reasoning |
| Journalism and
Misinformation Detection | Evaluate ChatGPT response
on conspiracy statements and
politically divided ideas [40] | Performed a descriptive study
on ChatGPT responses to
various COVID-19 vaccine
topics | ChatGPT was dismissive of
conspiracy statements but
remained neutral on
controversial political views
by stating pros and cons |
| Software Development | Evaluate ChatGPT’s response
to software testing questions
[41] | Asked ChatGPT to respond to
textbook questions in a
common software testing
curriculum | Only 37.5% of the questions
were correctly answered |
| Translation | Evaluate ChatGPT’s ability in
translation [42] | Used several benchmark test
sets to compare ChatGPT’s
responses in translating | Performs on par with
commercial applications for
high-resource European
languages but lags behind on
distant languages |
| Scientific Research | Write scientific and academic
papers [43] | Discussed several papers who
used and listed ChatGPT as
authors | Highlighted potential ethical
concerns |
|  | Automation in Economic
research [49] | Highlighted use cases of
ChatGPT in research,
including language editing
and headline generation | N/A |
|  | Summarize and translate
research papers for non-
native English speakers [50] | Used ChatGPT to summarize
and other AI tools to translate
Chinese written paper | Coherent writing style after
manual screening. Potential
benefit in speeding up
research but has several
ethical concerns |

---

## Página 11

ChatGPT may sound interesting and convincing, but don’t take its word for it! Indeed, ChatGPT’s ability 
in forming meaningful and conversational sentences is quite impressive, but it may often ‘hallucinate’ 
responses [56]. Therefore, it is strongly recommended to verify and fact-check any responses from 
ChatGPT. 
ChatGPT makes errors in simple reasoning, logic, mathematics, and presenting factual information [57]. 
It is likely that the next version of GPT-4, expected to be released sometime in 2023, will significantly 
improve ChatGPT. According to several sources, GPT-4 network will be far more complex than its 
predecessor containing around 100 trillion parameters5. The GPT-3 model, in comparison, is made up of 
175 billion parameters. 
ChatGPT is currently limited in processing a maximum of 5000 tokens of text as input. While this is not 
a problem in most applications, it can be challenging in tasks like text summarization. Moreover, the current 
interface of ChatGPT does not allow uploading images or audio files. ChatGPT can produce code 
representations of visual images based on text prompts, but its drawing skills are somewhat limited 
currently [38]. Recently, there have been attempts in using a combination of prompts and data files to create 
a multi-input model that can perform text, visual and audio tasks using AI6. 
ChatGPT has a tendency to give wordy and detailed responses unless explicitly asked not to. Moreover, 
ChatGPT expresses fewer emotions than an average human and tends to be more objective [58]. Therefore, 
ChatGPT cannot replace the need for human connection or be your friend! Similarly, it cannot be used for 
personal therapy or counseling, which require an intimate human connection. 
Although ChatGPT can fetch you information about an incident prior to September 2021, do not expect 
it to give you the latest news! When asked about the recent Earthquake in Turkey, ChatGPT replies: ‘I'm 
sorry, but as an AI language model, I do not have access to information from the future. As of my knowledge 
cutoff date of September 2021, there had not been any significant earthquakes in Turkey in 2023. However, 
earthquakes can occur at any time, and it's important to be prepared and informed about potential risks 
and safety measures.’ 
 
Question: Hi ChatGPT, what are some of your limitations? 
ChatGPT: As an AI language model, I have some limitations, some of which include: 
 
1) Limited context: While I can understand and respond to a wide range of topics and questions, my 
responses are limited to the information and context provided in the question or statement. I do not have 
the ability to understand context beyond the given information. 
2) Lack of emotion and empathy: I do not have emotions, and I cannot empathize with the user or 
understand their feelings. 
 
5 https://www.forbes.com/sites/bernardmarr/2023/02/24/gpt-4-is-coming--what-we-know-so-far/?sh=206f0ae86c2d 
6 https://aianswerz.com/

---

## Página 12

3) Inability to interpret nonverbal cues: As an AI language model, I do not have the ability to interpret 
nonverbal cues, such as body language or facial expressions, which are essential in human 
communication. 
4) Dependence on data quality: My responses are only as good as the data used to train me. If the data 
used to train me is biased or incomplete, my responses may also be biased or incomplete. 
5) Inability to perform physical tasks: I am a language model and do not have a physical body, so I 
cannot perform physical tasks or interact with the physical world in any way. 
 
5. Concluding Remarks: Consideration for Ethical and Privacy Concerns 
In this paper, we provided a historical overview on the development chatbots. In addition, we looked at 
the significant technological developments that enabled the emergence and success of ChatGPT. We then 
described the potential of ChatGPT in several domains and applications. In healthcare, ChatGPT can 
potentially be used for medical screening, answering general questions, and exam preparation. In education, 
ChatGPT can be used in tutoring and detecting plagiarism. ChatGPT can also aid researchers with writing, 
summarizing information, and translating. However, there are many ethical and privacy concerns that needs 
to be addressed about ChatGPT. For instance, some users have reported ChatGPT’s responses containing 
race and gender bias7. Moreover, given its effectiveness, ChatGPT may be used for unethical purposes in 
education, including cheating. In research, ChatGPT raises ethical questions about copyright and 
plagiarism. In terms of privacy concerns, ChatGPT is trained with more than 300 billion words, potentially 
containing personal information of internet users8. Finally, ChatGPT continues to improve from user 
interaction, but prompts containing personal information, such as contact, may be processed and even learnt 
by the model. 
Acknowledgements 
The authors would like to thank ChatGPT for providing thoughtful responses to our interview questions. 
Besides the interview responses, no other part of this manuscript was written by ChatGPT. 
Author statements 
Ethical Approval 
Ethical approval was not required because no personal data was used. Any analysis presented were 
aggregated. 
 
7 https://www.businessinsider.com/sam-altmans-chatgpt-has-a-bias-problem-that-could-get-it-canceled-2023-2 
8 https://arstechnica.com/information-technology/2023/02/chatgpt-is-a-data-privacy-nightmare-and-you-ought-to-be-
concerned/

---

## Página 13

Competing Interests 
None declared. 
References 
[1] 
A. M. TURING, “I.—COMPUTING MACHINERY AND INTELLIGENCE,” Mind, vol. LIX, no. 
236, pp. 433–460, Oct. 1950, doi: 10.1093/mind/LIX.236.433. 
[2] 
J. Weizenbaum, “ELIZA—a computer program for the study of natural language communication 
between man and machine,” Commun. ACM, vol. 9, no. 1, pp. 36–45, 1966. 
[3] 
G. Güzeldere and S. Franchi, “Dialogues with colorful ‘personalities’ of early AI,” Stanf. Humanit. 
Rev., vol. 4, no. 2, pp. 161–169, 1995. 
[4] 
A. Pinar Saygin, I. Cicekli, and V. Akman, “Turing Test: 50 Years Later,” Minds Mach., vol. 10, no. 
4, pp. 463–518, Nov. 2000, doi: 10.1023/A:1011288000451. 
[5] 
B. Luo, R. Y. K. Lau, C. Li, and Y.-W. Si, “A critical review of state-of-the-art chatbot designs and 
applications,” WIREs Data Min. Knowl. Discov., vol. 12, no. 1, p. e1434, 2022, doi: 
10.1002/widm.1434. 
[6] 
E. Adamopoulou and L. Moussiades, “An Overview of Chatbot Technology,” in Artificial 
Intelligence Applications and Innovations, Cham, 2020, pp. 373–383. doi: 10.1007/978-3-030-
49186-4_31. 
[7] 
B. R. Ranoliya, N. Raghuwanshi, and S. Singh, “Chatbot for university related FAQs,” in 2017 
International Conference on Advances in Computing, Communications and Informatics (ICACCI), 
Sep. 2017, pp. 1525–1530. doi: 10.1109/ICACCI.2017.8126057. 
[8] 
A. M. Rahman, A. A. Mamun, and A. Islam, “Programming challenges of chatbot: Current and future 
prospective,” in 2017 IEEE Region 10 Humanitarian Technology Conference (R10-HTC), Dec. 2017, 
pp. 75–78. doi: 10.1109/R10-HTC.2017.8288910. 
[9] 
L. Zhou, J. Gao, D. Li, and H.-Y. Shum, “The Design and Implementation of XiaoIce, an Empathetic 
Social Chatbot,” Comput. Linguist., vol. 46, no. 1, pp. 53–93, Mar. 2020, doi: 10.1162/coli_a_00368. 
[10] A. Følstad and P. B. Brandtzaeg, “Users’ experiences with chatbots: findings from a questionnaire 
study,” Qual. User Exp., vol. 5, no. 1, p. 3, Apr. 2020, doi: 10.1007/s41233-020-00033-2. 
[11] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training of deep bidirectional 
transformers for language understanding,” in Proceedings of the 2019 conference of the north 
american chapter of the association for computational linguistics: Human language technologies, 
volume 1 (long and short papers), 2019, pp. 4171–4186. 
[12] A. Radford et al., “Language models are unsupervised multitask learners,” OpenAI Blog, vol. 1, no. 
8, p. 9, 2019. 
[13] T. Brown et al., “Language models are few-shot learners,” in Advances in neural information 
processing 
systems, 
2020, 
vol. 
33, 
pp. 
1877–1901. 
[Online]. 
Available: 
https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf 
[14] H. H. Thorp, “ChatGPT is fun, but not an author,” Science, vol. 379, no. 6630, pp. 313–313, Jan. 
2023, doi: 10.1126/science.adg7879. 
[15] H. Else, “Abstracts written by ChatGPT fool scientists,” Nature, vol. 613, no. 7944, pp. 423–423, 
Jan. 2023, doi: 10.1038/d41586-023-00056-7. 
[16] L. De Angelis et al., “ChatGPT and the Rise of Large Language Models: The New AI-Driven 
Infodemic Threat in Public Health.” Rochester, NY, Feb. 09, 2023. doi: 10.2139/ssrn.4352931. 
[17] R. A. Khan, M. Jawaid, A. R. Khan, and M. Sajjad, “ChatGPT - Reshaping medical education and 
clinical management,” Pak. J. Med. Sci., vol. 39, no. 2, Feb. 2023, doi: 10.12669/pjms.39.2.7653. 
[18] A. Rao, J. Kim, M. Kamineni, M. Pang, W. Lie, and M. D. Succi, “Evaluating ChatGPT as an Adjunct 
for Radiologic Decision-Making.” medRxiv, p. 2023.02.02.23285399, Feb. 07, 2023. doi: 
10.1101/2023.02.02.23285399. 
[19] A. T. Gabrielson, A. Y. Odisho, and D. Canes, “Harnessing Generative AI to Improve Efficiency 
Among Urologists: Welcome ChatGPT,” J. Urol., vol. 0, no. 0, p. 10.1097/JU.0000000000003383, 
Feb. 2023, doi: 10.1097/JU.0000000000003383. 
[20] A. Hulman et al., “ChatGPT- versus human-generated answers to frequently asked questions about 
diabetes: a Turing test-inspired survey among employees of a Danish diabetes center.” medRxiv, p. 
2023.02.13.23285745, Feb. 15, 2023. doi: 10.1101/2023.02.13.23285745.

---

## Página 14

[21] Y. Zhu, D. Han, S. Chen, F. Zeng, and C. Wang, “How Can ChatGPT Benefit Pharmacy: A Case 
Report on Review Writing.” Preprints, Feb. 20, 2023. doi: 10.20944/preprints202302.0324.v1. 
[22] Y. Shen et al., “ChatGPT and Other Large Language Models Are Double-edged                     Swords,” 
Radiology, p. 230163, Jan. 2023, doi: 10.1148/radiol.230163. 
[23] T. H. Kung et al., “Performance of ChatGPT on USMLE: Potential for AI-assisted medical education 
using large language models,” PLOS Digit. Health, vol. 2, no. 2, p. e0000198, Feb. 2023, doi: 
10.1371/journal.pdig.0000198. 
[24] X. Wang et al., “ChatGPT Performs on the Chinese National Medical Licensing Examinatio.” 2023. 
doi: 10.21203/rs.3.rs-2584079/v1. 
[25] F. Antaki, S. Touma, D. Milad, J. El-Khoury, and R. Duval, “Evaluating the Performance of 
ChatGPT in Ophthalmology: An Analysis of its Successes and Shortcomings.” medRxiv, p. 
2023.01.22.23284882, Jan. 26, 2023. doi: 10.1101/2023.01.22.23284882. 
[26] N. Fijačko, L. Gosak, G. Štiglic, C. T. Picard, and M. J. Douma, “Can ChatGPT pass the life support 
exams without entering the American heart association course?,” Resuscitation, vol. 0, no. 0, Feb. 
2023, doi: 10.1016/j.resuscitation.2023.109732. 
[27] A. B. Mbakwe, I. Lourentzou, L. A. Celi, O. J. Mechanic, and A. Dagan, “ChatGPT passing USMLE 
shines a spotlight on the flaws of medical education,” PLOS Digit. Health, vol. 2, no. 2, p. e0000205, 
Feb. 2023, doi: 10.1371/journal.pdig.0000205. 
[28] S. Shahriar, J. Ramesh, M. Towheed, T. Ameen, A. Sagahyroon, and A. R. Al-Ali, “Narrative 
Integrated Career Exploration Platform,” Front. Educ., vol. 7, 2022, Accessed: Feb. 21, 2023. 
[Online]. Available: https://www.frontiersin.org/articles/10.3389/feduc.2022.798950 
[29] E. Kasneci et al., “ChatGPT for Good? On Opportunities and Challenges of Large Language Models 
for Education.” EdArXiv, Jan. 29, 2023. doi: 10.35542/osf.io/5er8f. 
[30] J. Rudolph, S. Tan, and S. Tan, “ChatGPT: Bullshit spewer or the end of traditional assessments in 
higher education?,” J. Appl. Learn. Teach., vol. 6, no. 1, Art. no. 1, Jan. 2023, doi: 
10.37074/jalt.2023.6.1.9. 
[31] B. D. Lund and T. Wang, “Chatting about ChatGPT: how may AI and GPT impact academia and 
libraries?,” Libr. Hi Tech News, vol. ahead-of-print, no. ahead-of-print, Jan. 2023, doi: 
10.1108/LHTN-01-2023-0009. 
[32] D. Mhlanga, “Open AI in Education, the Responsible and Ethical Use of ChatGPT Towards Lifelong 
Learning.” Rochester, NY, Feb. 11, 2023. doi: 10.2139/ssrn.4354422. 
[33] Z. A. Pardos and S. Bhandari, “Learning gain differences between ChatGPT and human tutor 
generated algebra hints.” arXiv, Feb. 14, 2023. doi: 10.48550/arXiv.2302.06871. 
[34] S. Frieder et al., “Mathematical Capabilities of ChatGPT.” arXiv, Jan. 31, 2023. doi: 
10.48550/arXiv.2301.13867. 
[35] M. Khalil and E. Er, “Will ChatGPT get you caught? Rethinking of Plagiarism Detection.” arXiv, 
Feb. 08, 2023. doi: 10.48550/arXiv.2302.04335. 
[36] X. Yang, Y. Li, X. Zhang, H. Chen, and W. Cheng, “Exploring the Limits of ChatGPT for Query or 
Aspect-based Text Summarization.” arXiv, Feb. 15, 2023. doi: 10.48550/arXiv.2302.08081. 
[37] Z. Basic, A. Banovac, I. Kruzic, and I. Jerkovic, “Better by you, better than me, chatgpt3 as writing 
assistance in students essays.” arXiv, Feb. 09, 2023. doi: 10.48550/arXiv.2302.04536. 
[38] Y. Bang et al., “A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, 
Hallucination, and Interactivity.” arXiv, Feb. 08, 2023. doi: 10.48550/arXiv.2302.04023. 
[39] K. Hayawi, S. Shahriar, M. A. Serhani, I. Taleb, and S. S. Mathew, “ANTi-Vax: a novel Twitter 
dataset for COVID-19 vaccine misinformation detection,” Public Health, vol. 203, pp. 23–30, Feb. 
2022, doi: 10.1016/j.puhe.2021.11.022. 
[40] M. Sallam et al., “ChatGPT Output Regarding Compulsory Vaccination and COVID-19 Vaccine 
Conspiracy: A Descriptive Study at the Outset of a Paradigm Shift in Online Search for Information,” 
Cureus, vol. 15, no. 2, p. e35029, Feb. 2023, doi: 10.7759/cureus.35029. 
[41] S. Jalil, S. Rafi, T. D. LaToza, K. Moran, and W. Lam, “ChatGPT and Software Testing Education: 
Promises & Perils.” arXiv, Feb. 08, 2023. doi: 10.48550/arXiv.2302.03287. 
[42] W. Jiao, W. Wang, J. Huang, X. Wang, and Z. Tu, “Is ChatGPT A Good Translator? A Preliminary 
Study.” arXiv, Jan. 31, 2023. doi: 10.48550/arXiv.2301.08745. 
[43] C. Stokel-Walker, “ChatGPT listed as author on research papers: many scientists disapprove,” 
Nature, vol. 613, no. 7945, pp. 620–621, Jan. 2023, doi: 10.1038/d41586-023-00107-z. 
[44] S. H. Park, “Authorship Policy of the Korean Journal of Radiology Regarding Artificial Intelligence 
Large Language Models Such as ChatGTP,” Korean J. Radiol., vol. 24, no. 3, pp. 171–172, Mar. 
2023, doi: 10.3348/kjr.2023.0112.

---

## Página 15

[45] J. Thornton, R. D’Souza, and R. Tandon, “Artificial intelligence and psychiatry research and 
practice,” Asian J. Psychiatry, p. 103509, Feb. 2023, doi: 10.1016/j.ajp.2023.103509. 
[46] S. Polesie and O. Larkö, “Use of Large Language Models: Editorial Comments,” Acta Derm. 
Venereol., vol. 103, p. adv00874, Feb. 2023, doi: 10.2340/actadv.v103.9593. 
[47] G. Tang, “Letter to editor: Academic journals should clarify the proportion of NLP-generated content 
in papers,” Account. Res., vol. 0, no. 0, pp. 1–2, Feb. 2023, doi: 10.1080/08989621.2023.2180359. 
[48] B. Aczel and E.-J. Wagenmakers, “Transparency Guidance for ChatGPT Usage in Scientific 
Writing.” PsyArXiv, Feb. 06, 2023. doi: 10.31234/osf.io/b58ex. 
[49] A. Korinek, “Language Models and Cognitive Automation for Economic Research.” National Bureau 
of Economic Research, Feb. 2023. doi: 10.3386/w30957. 
[50] T.-J. Chen, “ChatGPT and other artificial intelligence applications speed up scientific writing,” J. 
Chin. Med. Assoc., p. 10.1097/JCMA.0000000000000900, doi: 10.1097/JCMA.0000000000000900. 
[51] Ö. Aydın and E. Karaarslan, “OpenAI ChatGPT Generated Literature Review: Digital Twin in 
Healthcare.” Rochester, NY, Dec. 21, 2022. doi: 10.2139/ssrn.4308687. 
[52] M. Dowling and B. Lucey, “ChatGPT for (Finance) research: The Bananarama Conjecture,” Finance 
Res. Lett., p. 103662, Jan. 2023, doi: 10.1016/j.frl.2023.103662. 
[53] C. Stokel-Walker and R. Van Noorden, “What ChatGPT and generative AI mean for science,” 
Nature, vol. 614, no. 7947, pp. 214–216, Feb. 2023, doi: 10.1038/d41586-023-00340-6. 
[54] J. Y. Lee, “Can an artificial intelligence chatbot be the author of a scholarly article?,” Sci. Ed., vol. 
10, no. 1, pp. 7–12, Feb. 2023, doi: https://doi.org/10.6087/kcse.292. 
[55] Z. Lin, “Why and how to embrace AI such as ChatGPT in your academic life.” PsyArXiv, Feb. 05, 
2023. doi: 10.31234/osf.io/sdx3j. 
[56] H. Alkaissi and S. I. McFarlane, “Artificial Hallucinations in ChatGPT: Implications in Scientific 
Writing,” Cureus, vol. 15, no. 2, p. e35179, Feb. 2023, doi: 10.7759/cureus.35179. 
[57] A. Borji, “A Categorical Archive of ChatGPT Failures.” arXiv, Feb. 21, 2023. doi: 
10.48550/arXiv.2302.03494. 
[58] B. Guo et al., “How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and 
Detection.” arXiv, Jan. 18, 2023. doi: 10.48550/arXiv.2301.07597.

---

