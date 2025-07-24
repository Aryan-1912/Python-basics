feedback = ["great service", "nice", "good", "excellent service", "worst"]

feedback.append("bad food")
feedback.append("worsstest")

print(feedback)
# countin +feed

positive = sum(1 for comment in feedback if "good" in comment.lower() or "excellent" in comment.lower())

print (f"positive feedback count : {positive}")

#all feedback

for comment in feedback:
    print(f"-{comment}")