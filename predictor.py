# -*- coding: utf-8 -*-
"""predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g3ezzyEHJ44aydl-Rxg_ShdaZb5nMhEj
"""

pip install transformers

import pandas as pd
import pickle
import transformers
import tqdm
from keras.preprocessing import sequence

title = "BRUSSELS (Reuters) - Britain and the European Union have agreed on the three key divorce issues of a financial settlement, citizens  rights and how to avoid a hard border between Ireland and Northern Ireland after Britain leaves the EU, a joint report said. The report did not specify a sum that Britain would owe the EU as a result of its exit from the bloc in 2019, but said:  Both Parties have agreed a methodology for the financial settlement.  On Northern Ireland, the report said that unless otherwise agreed, Britain would keep laws in Northern Ireland aligned with those of the European Union s internal market and customs union to avoid the need for a border.  In the absence of agreed solutions, the United Kingdom will maintain full alignment with those rules of the Internal Market and the Customs Union which, now or in the future, support North-South cooperation, the all island economy and the protection of the 1998 Agreement,  the report said. ";
text = "BEIJING (Reuters) - Whether President-elect Donald Trump goes through with a deployment of a U.S. anti-missile system in South Korea will be a key indicator to how political ties unfold with China, sources with ties to the leadership in Beijing said. Beijing will also be keeping a close eye on Trumpâ€™s meeting on Thursday with Prime Minister Shinzo Abe of Japan, its key regional rival, for clues on how the President-elect, who has never held public office, is likely to conduct foreign policy, they said. South Korea and the United States have agreed to deploy a Terminal High Altitude Area Defence (THAAD) anti-missile system  to counter missile threats from North Korea. It is expected to be in place within eight to 10 months, the commander of U.S. forces in South Korea said earlier this month. China has argued the planned deployment undermines strategic stability in Northeast Asia, and worries that THAADâ€™s powerful radar provides coverage of Chinaâ€™s missile installations. â€œWhether deployment of the Terminal High Altitude Area Defense is delayed is a political weather vane,â€ one source said. A security adviser to Trump said last week his meeting in New York with Abe on Thursday may mark the start of talks to garner Tokyoâ€™s support for a push-back against Chinaâ€™s growing influence in Asia. â€œWe have heard what he said. We will now watch what he does,â€ said the source, requesting anonymity because he is not authorized to speak to media. â€œWe will play it by ear,â€ the source said, invoking an idiom that translates to blocking a punch or a kick as it comes. Trump has created doubts over his commitment to security alliances with Japan and South Korea, suggesting they need to pay more for a U.S. military presence and even hinting they should develop their own nuclear weapons capability. Japan going nuclear would be Chinaâ€™s worst nightmare and is likely to provoke strong reaction, diplomats and analysts have said. Chinaâ€™s relations with Japan have long been poisoned by what Beijing sees as Tokyoâ€™s failure to fully atone for its invasion and occupation of parts of China before and during World War Two as well as competing claims over a group of East China Sea islets. â€œNortheast Asia would be a powder keg,â€ a second source said, referring to a nuclearized sub-region including China, Japan, North and South Korea. The State Council Information Office, or cabinet spokesmanâ€™s office, had no immediate comment. China is generally opposed to military alliances, seeing them as Cold War relics.  Chinaâ€™s stability-obsessed leaders do not know what to make of the 70-year-old Trump, whose win over Hillary Clinton was unexpected, and has backpedaled on some of his more controversial campaign statements. For example, Trump pledged his commitment to defending South Korea under an existing security alliance during a phone call last week with South Korean President Park Geun-hye. Trump had said during the election campaign he would be willing to withdraw the 28,500 U.S. troops stationed in South Korea unless Seoul paid a greater share of the cost of the U.S. deployment. Trump told Reuters in an interview in May he was willing to talk to North Korean leader Kim Jong Un to try to stop Pyongyangâ€™s nuclear program - a major shift in U.S. policy toward the isolated nation - but has also called for China to do more to rein in Pyongyang. Sino-U.S. relations after Trump takes office on Jan. 20 are expected to be fluid, although Chinese President Xi Jinping told Trump during a telephone call on Monday cooperation was the â€œonly correct choiceâ€ for the two giants. A statement from Trumpâ€™s presidential transition office said the two men â€œestablished a clear sense of mutual respect for one anotherâ€ and he believes the two countries will have one of the strongest relationships moving forward. Trumpâ€™s election does offer some good news for China: it signals the demise of the U.S.-led Trans-Pacific Partnership (TPP), which excludes China; it raises the possibility of belated U.S. backing for the China-led Asian Infrastructure Investment Bank, and possibly marks an end to President Obamaâ€™s strategic â€œpivotâ€ to Asia. The bad news is that Trump has often made provocative remarks about China during his campaign, including threats to slap 45 percent tariffs on imports from China and label the worldâ€™s second-biggest economy a currency manipulator. Wei Jianguo, a retired vice commerce minister, was optimistic a trade war could be avoided. â€œProtectionism is on the rise, but a trade war between China and the United States is unlikely,â€ Wei, vice chairman of the China Center for International Economic Exchanges, a government-backed think-tank, told Reuters. â€œThat was just election rhetoric,â€ he said. ";
subject = "(Reuters) - Highlights of the day for U.S. President Donald Trumpâ€™s administration on Wednesday: Trump urges Senate Republicans to â€œgo nuclearâ€ and impose a rule change to force a simple majority vote toward confirmation if Democrats block his U.S. Supreme Court nominee. Public refusals by two U.S. Senate Republicans to support Betsy DeVos, Trumpâ€™s pick for education secretary, raise the possibility of a rare congressional rejection of a Cabinet nominee. The Senate confirms Rex Tillerson as secretary of state despite concerns over his ties to Russia, while committees approve Jeff Sessions, one of Trumpâ€™s most controversial Cabinet selections, as attorney general, as well as two other nominees. Evangelical Christian leader Jerry Falwell Jr. will head an education reform task force under Trump and is eager to cut university regulations, including rules on dealing with campus sexual assault. The White House puts Iran â€œon noticeâ€ for test-firing a ballistic missile and says it is reviewing how to respond, abruptly adopting an aggressive posture toward Tehran that could raise tensions in the region. Defense Secretary James Mattis is expected to underscore security commitments to South Korea and Japan on his debut trip to Asia this week as concerns mount over North Koreaâ€™s missile program and tensions with China. Tillerson sees his job become harder before it even begins because of administration moves that have antagonized Muslim nations, European allies, Mexico and U.S. bureaucrats. The Trump administration wants to revamp and rename a U.S. government program designed to counter all violent ideologies so that it focuses solely on Islamist extremism, five people briefed on the matter tell Reuters. Trump pays his respects to a U.S. Navy SEAL who died in a raid on al Qaeda in Yemen that went wrong, the first military operation authorized by Trump as commander in chief. Trump will likely face questions about his executive order restricting some travel to the United States when he meets with the CEOs of major U.S. companies at the White House on Friday. U.N. human rights experts warn that asylum seekers could face torture if not given haven and the Vatican calls for  openness to other cultures, adding to a drumbeat of criticism of Trumpâ€™s travel curbs. Trump lashes out at one of his favorite targets for derision - the news media - complaining to a group of his supporters attending a Black History Month session that most reporters who cover him are a â€œdisgrace.â€ ";
date = "February 1, 2017";

df = pd.DataFrame([[title,text,subject,date]]
                              ,columns=['title', 'text', 'subject', 'date']
                                  )

x = df['text']

import transformers
def func_tokenizer(tokenizer_name, docs):
    features = []
    for doc in tqdm.tqdm(docs, desc = 'converting documents to features'):
        tokens = tokenizer_name.tokenize(doc)
        ids = tokenizer_name.convert_tokens_to_ids(tokens)
        features.append(ids)
    return features
print("The function is created successfully")
roberta_tokenizer = transformers.RobertaTokenizer.from_pretrained('roberta-base-openai-detector')

with open(f'modelxgb.pkl', 'rb') as f:
  xgb = pickle.load(f)

roberta_tokenizer = transformers.RobertaTokenizer.from_pretrained('roberta-base-openai-detector')

roberta_test_features = func_tokenizer(roberta_tokenizer, x)

roberta_test = sequence.pad_sequences(roberta_test_features, maxlen = 500)


xgb_pred = xgb.predict(roberta_test)
print("\n")
print(xgb_pred)