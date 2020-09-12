def disp(**kw):
    print(type(kw))
    for k,v in kw.items():
        print(k, v)


disp(a=10, b=20, c=30)