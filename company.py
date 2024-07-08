import streamlit as st
from database import get_db_connection
from PIL import Image


def about_us():
    st.title("About Us")
    image = Image.open('images/promo_stock.jpg')
    st.image(image)
    conn = get_db_connection()
    cursor = conn.cursor()

    st.subheader('Our Style')
    content = 'At Serenity, we believe in the timeless appeal of simplicity and the power of versatility. Our style philosophy centers on crafting high-quality, essential pieces that form the backbone of any wardrobe. ' \
              'By focusing on clean lines, classic silhouettes, and premium materials, we create clothing that transcends trends and stands the test of time. ' \
              'Each item is thoughtfully designed to offer comfort, functionality, and effortless style, ensuring that our customers can seamlessly transition from day to night, from work to play. ' \
              'We celebrate individuality by providing a blank canvas that allows personal expression through endless possibilities of styling. ' \
              'At Serenity, our commitment is to provide you with foundational pieces that you can rely on, season after season.'

    st.write(content)

    st.subheader('As a Business')
    cursor.execute("SELECT content FROM about_us")
    about_us_content = cursor.fetchone()
    conn.close()
    st.write(about_us_content[0])

    st.subheader('Our Purpose')
    content2 = ('Our purpose at Serenity is to create clothing that simplifies and enriches our customers\' lives. We '
                'strive to offer wardrobe staples that are not only stylish but also durable, allowing our customers '
                'to express themselves effortlessly.')

    st.write(content2)

    st.subheader('Meet the Team')
    team_members = [
        {"name": "Tony Vazquez", "role": "Backend Developer/Database Administrator",
         "bio": "Tony Vasquez is a seasoned backend developer and database administrator known for his expertise in "
                "architecting scalable solutions and optimizing database performance. With a solid foundation in SQL "
                "and NoSQL databases, Tony specializes in designing efficient database schemas that ensure data "
                "integrity and support seamless application functionality. He brings extensive experience in backend "
                "technologies such as Python, Django, and MongoDB, leveraging his skills to enhance data workflows "
                "and maintain high standards of security. Tony is passionate about crafting robust backend systems "
                "that drive operational efficiency and deliver exceptional user experiences. His collaborative "
                "approach and problem-solving abilities make him an asset to any development team."},
        {"name": "Anthony Lleo", "role": "Frontend Developer",
         "bio": "Anthony Lleo is a dedicated frontend developer with a passion for crafting intuitive and visually "
                "appealing user interfaces. Proficient in HTML, CSS, and JavaScript frameworks such as React and "
                "Vue.js, Anthony excels in translating design concepts into responsive and functional web "
                "applications. He combines creativity with technical expertise to create seamless user experiences "
                "that resonate with users. Anthony is skilled in optimizing frontend performance and accessibility, "
                "ensuring that applications meet modern web standards. With a commitment to continuous learning and "
                "staying updated with industry trends, Anthony brings innovation and efficiency to every project he "
                "undertakes."},
        {"name": "Angie Martinez", "role": "Software Architect/Product Manager",
         "bio": "Angie Martinez is a versatile professional with a dual focus on software architecture and product "
                "management. With a background in computer science and design, Angie blends technical expertise with "
                "a keen understanding of user experience (UX) and product strategy. She excels in frontend "
                "technologies such as HTML, CSS, JavaScript, and Angular, leveraging her skills to create compelling "
                "user interfaces and optimize frontend performance. As a product manager, Angie drives product vision "
                "and strategy, leading cross-functional teams to deliver innovative solutions that meet market needs "
                "and exceed customer expectations. Her collaborative approach, strong communication skills, "
                "and passion for user-centric design make her an invaluable asset in achieving business objectives "
                "and driving product success."},
        {"name": "Luis Isaac", "role": "Frontend Developer",
         "bio": "Luis Isaac is a passionate frontend developer with a strong foundation in web technologies and user "
                "interface design. Proficient in HTML, CSS, and JavaScript frameworks such as React and Bootstrap, "
                "Luis specializes in creating responsive and user-friendly web applications. He combines his "
                "technical skills with a keen eye for design aesthetics to deliver visually appealing and functional "
                "interfaces that enhance user experience. Luis is dedicated to continuous learning and staying "
                "updated with the latest frontend trends and best practices, ensuring that his work meets modern web "
                "standards. With a collaborative mindset and a focus on delivering high-quality solutions, "
                "Luis contributes to the success of projects by translating client requirements into engaging digital "
                "experiences."}
    ]

    for member in team_members:
        st.write(f"**{member['name']}** - {member['role']}")
        st.write(member['bio'])


def contact_us():
    st.title("Contact Us")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM contact_us")
    contact_us_content = cursor.fetchone()
    conn.close()
    st.write(contact_us_content[0])
