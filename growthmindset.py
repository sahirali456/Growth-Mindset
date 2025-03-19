import streamlit as st

st.set_page_config(page_title="Growth Mindset Web App", layout="wide")

st.title("Growth Mindset Web App")
st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to:", ["Home", "Why Growth Mindset?", "Practical Tips"])

if page == "Home":
    st.header("What is Growth Mindset?")
    st.write("A growth mindset means you can learn, improve, and groove.")
    st.image("C:\\Users\\classic computer 220\\Desktop\\Sahir ali\\2.jpg", caption="Growth Mindset", use_container_width=True)
    
    st.subheader("What is Growth Mindset?")
    st.write("A growth mindset is the belief that intelligence, abilities, and skills can be developed through effort, learning, and persistence. This idea was introduced by psychologist Carol Dweck, who contrasted it with a fixed mindset, which is the belief that intelligence and talent are unchangeable. People with a growth mindset see challenges as opportunities, learn from failures, and continuously improve. For example, a student struggling with math can either believe they are bad at math (fixed mindset) or view the struggle as a chance to grow by practicing more and seeking help (growth mindset). Carol Dweck encourages this by saying that people should love challenges, be intrigued by mistakes, enjoy effort, and keep on learning.")
    st.write("Quote: Love challenges, be intrigued by mistakes, enjoy effort, and keep on learning. Carol Dweck ")
    
    st.subheader("Challenges and Learning from Failure")
    st.write("One key aspect of a growth mindset is embracing challenges and learning from failure rather than fearing it. People with a growth mindset do not see mistakes as proof of incompetence but as stepping stones to mastery. Consider Thomas Edison, who failed thousands of times before inventing the light bulb. Instead of being discouraged, he famously said that he had not failed but had simply found 10,000 ways that would not work. This approach is vital not only in academics but also in personal and professional life. Athletes, sc  d entrepreneurs all succeed by treating setbacks as valuable learning experiences.")
    st.write("Quote: I have not failed. I've just found 10,000 ways that won’t work. – Thomas Edison")
    
    st.subheader("Effort Over Talent")
    st.write("A growth mindset emphasizes hard work and persistence over natural talent. Many people believe that geniuses are simply born gifted, but research shows that consistent effort plays a much larger role in success. For example, Michael Jordan, one of the greatest basketball players of all time, was cut from his high school basketball team. Instead of giving up, he practiced tirelessly and turned failure into motivation. This mindset helps individuals push through difficulties instead of giving up when things do not come easily.")
    st.write("Quote: I can accept failure, everyone fails at something. But I can’t accept not trying. – Michael Jordan")
    
    st.subheader("The Power of Yet")
    st.write("One simple but powerful way to develop a growth mindset is by using the word yet. When faced with difficulties, instead of saying I can’t do this, say I can’t do this yet. This small shift in thinking reinforces that improvement is always possible with time and effort. For instance, if a programmer is struggling to learn a new coding language, a fixed mindset might lead them to believe they are just not good at programming. But a growth mindset would remind them that with practice, feedback, and persistence, they can improve.")
    st.write("Quote: Becoming is better than being. – Carol Dweck")
    
    st.subheader("Applying Growth Mindset in Daily Life")
    st.write("A growth mindset is not just for school or work; it applies to all areas of life. Whether learning a new skill, overcoming personal challenges, or striving for a healthier lifestyle, the ability to persist and adapt is crucial. A person trying to lose weight, for example, may face setbacks, but instead of quitting, they can analyze what went wrong and adjust their approach. Similarly, in relationships, a growth mindset helps people learn from conflicts and improve communication. By believing in continuous improvement, individuals become more resilient, adaptable, and successful in their endeavors.")
    st.write("Quote: Whether you think you can, or you think you can’t – you’re right. – Henry Ford")

elif page == "Why Growth Mindset?":
    st.header("Why Should You Develop a Growth Mindset?")
    
    st.subheader("Overcoming Challenges and Obstacles")
    st.write("A growth mindset helps individuals view challenges as opportunities rather than barriers. When people believe they can improve through effort, they are more likely to take on difficult tasks and persist despite setbacks. Consider J.K. Rowling, who was rejected by multiple publishers before 'Harry Potter' became a global success. Had she given up, millions would have never experienced her magical world. A growth mindset encourages resilience and determination in the face of adversity.")
    st.write("Quote: It is our choices that show what we truly are, far more than our abilities. – J.K. Rowling")
    
    st.subheader("Boosting Self-Confidence and Motivation")
    st.write("People with a growth mindset have higher self-confidence because they understand that improvement is within their control. Instead of fearing failure, they see effort as the path to success. This increases motivation and leads to consistent progress. Serena Williams, one of the greatest tennis players, consistently practiced and refined her skills, demonstrating how effort and perseverance yield success.")
    st.write("Quote: The only way to prove that you’re a good sport is to lose. – Ernie Banks")
    
    st.subheader("Encouraging Lifelong Learning")
    st.write("A fixed mindset can limit personal and professional growth, while a growth mindset encourages continuous learning. People with this mindset seek out new knowledge, embrace feedback, and view every experience as a learning opportunity. Bill Gates, for example, constantly reads and learns from experts across different fields, believing that success comes from ongoing education and adaptation.")
    st.write("Quote: Once you stop learning, you start dying. – Albert Einstein")
    
    st.subheader("Building Stronger Relationships")
    st.write("A growth mindset also helps in personal relationships. People with this mindset communicate openly, accept constructive criticism, and strive to improve themselves and their relationships. Instead of thinking ‘I’m just bad at relationships,’ they believe they can learn how to be better partners, friends, and colleagues through effort and understanding.")
    st.write("Quote: We cannot become what we need to be by remaining what we are. – John C. Maxwell")
    
    st.subheader("Success in Career and Innovation")
    st.write("Innovation and career success thrive on a growth mindset. Whether you are an entrepreneur, scientist, or artist, progress requires learning from mistakes, adapting, and persisting. Elon Musk, for example, faced multiple failures with SpaceX and Tesla before achieving groundbreaking success. He attributes much of his success to constantly learning, iterating, and refusing to give up.")
    st.write("Quote: Failure is an option here. If things are not failing, you are not innovating enough. – Elon Musk")


elif page == "Practical Tips":
    st.header("How to practice a Growth Mindset?")
    st.subheader("1 Set a goal to discover something new.")
    st.write("Setting a goal to discover something new is a powerful way to foster personal growth and development. Rather than simply wanting to learn something new, it's crucial to be specific about what that new discovery is, whether it’s learning a new skill, exploring a different field, or diving into a hobby you’ve always been curious about. Breaking down this goal into smaller, manageable steps makes the process less overwhelming. For instance, if you're interested in a subject like AI, starting with the basics of machine learning before progressing to more complex topics can make learning more structured. Establishing a realistic time frame for when you want to achieve your goal ensures that you stay focused and can track progress. Ultimately, the journey toward discovery is just as valuable as the discovery itself, and persistence in the face of challenges is key.")
    st.subheader(" 2 Avoid negative thinking.")
    st.write("Avoiding negative thinking is essential for achieving success and maintaining a healthy mindset. Negative thoughts often limit potential and can prevent you from pursuing your goals. A helpful approach is to challenge negative thoughts by questioning their validity and whether they are based on facts or assumptions. Instead of focusing on problems, shift your mindset toward finding solutions, which encourages a proactive and constructive attitude. Practicing self-compassion is also important, as it helps combat feelings of self-doubt or failure that may arise during setbacks. Surrounding yourself with positive influences can further uplift your mindset, and mindfulness practices like meditation can provide a sense of clarity and calm, helping to distance yourself from negativity. By fostering a positive mental attitude, you’ll be better equipped to tackle challenges with resilience and optimism.")
    st.subheader("3 Enjoy the learning process.")
    st.write("The learning process should be enjoyed rather than viewed as a task or hurdle. Embracing curiosity is the first step toward making learning enjoyable; by asking questions and exploring new areas, you keep the process exciting and engaging. Celebrating small wins along the way provides motivation and reminds you of the progress you’ve made, even if it’s incremental. To keep learning dynamic and interesting, interact with the material in various ways, such as through online courses, projects, or community discussions. Balancing intense learning sessions with breaks and rest is essential to avoid burnout, as a well-rested mind is more effective in absorbing new information. Lastly, finding joy in the struggle is a powerful mindset shift. Rather than viewing challenges as setbacks, see them as opportunities for growth and skill development. By maintaining a positive and enjoyable approach to learning, you’ll find the journey itself to be fulfilling and rewarding.")

