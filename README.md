# **Challenge Lab: AWS Lambda Exercise**

Step to complete this challenge :

1. Start Lab 

2. Go to AWS Lambda and create function configure like image below (change the python version in 3.7, in image wrong)

![image](https://user-images.githubusercontent.com/55681442/184058131-8aab2bfb-d988-4172-86d0-e8f649de4c2e.png)

3. Go to S3 and create bucket configure like image below

![image](https://user-images.githubusercontent.com/55681442/184058335-647c4aaf-fd50-4657-b932-cf4dfec1bf50.png)
![image](https://user-images.githubusercontent.com/55681442/184058402-28b20e7e-8485-48c3-a0e3-d6e3d4cf7b15.png)
![image](https://user-images.githubusercontent.com/55681442/184058439-130a708e-afb3-4b5c-87f7-c105cb469bb0.png)
![image](https://user-images.githubusercontent.com/55681442/184058469-7f71785b-470b-4e3f-9be2-8125537bba5d.png)

4. Back to AWS Lambda and set trigger configure like image below

![image](https://user-images.githubusercontent.com/55681442/184058603-69707fce-9dd8-4fd4-9e94-d6c3016e5c4d.png)

5. Go to tab code, and copy code from this github (in file lambda.py)

![image](https://user-images.githubusercontent.com/55681442/184058729-d4435e1f-ce58-479c-a2e9-33238f5958cf.png)

6. In tab test click down arrow and configure test event. Set param like image below 

![image](https://user-images.githubusercontent.com/55681442/184058923-dc2ab201-06fa-41e0-8c2c-671ec4c36972.png)

7. In Tab layer add pandas package (use file python.zip in this github)

![image](https://user-images.githubusercontent.com/55681442/184059595-836e0a96-9ab4-4006-823f-ebd7231454b2.png)

8. Add layer AWSlambda-Python-Scipy 

![image](https://user-images.githubusercontent.com/55681442/184059807-367c70dc-4761-48a2-ae33-42398d5b2147.png)

9. Go to SNS service AWS, create topic

![image](https://user-images.githubusercontent.com/55681442/184060151-6440cc2c-d024-4fd3-880d-26ca9133539a.png)

10. Create subcriptions 

![image](https://user-images.githubusercontent.com/55681442/184060252-c9cd2193-2df2-4603-9d16-41146f28c701.png)

11. Open email search notification email from AWS, and click link to subs 

![image](https://user-images.githubusercontent.com/55681442/184060391-4b9038c9-7ceb-4177-9697-cc5c2f08c488.png)

![image](https://user-images.githubusercontent.com/55681442/184060440-3fd0af78-8649-48ff-9039-2f3a0fffe0c2.png)

12. Testing upload file .txt to bucket S3, and you will get notification in email 

![image](https://user-images.githubusercontent.com/55681442/184060590-cf9c5bcb-4c11-416f-9ea1-b726092b90d0.png)

Note :
1. Make sure region in S3, Lambda and SNS same
2. Change the s3 name in code if the s3 name already exist
3. Setup python in lambda in version 3.7 (pandas file only support for that version)
4. Change TopicArn to Topic Arn in AWS SNS Topic


