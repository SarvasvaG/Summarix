def summarize(input, size,pipe,style):
    
    step = 1500
    k = 0
    l = step

    max_summary_length = 300

    if size == "Small":
        step = 2500
        max_summary_length = 50
    if size == "Medium":
        step = 1800
        max_summary_length = 100
    if size == "Large":
        step = 1000
        max_summary_length = 200

    output = ""

    for i in range(k, len(input), step):
        seg = input[k:l]
        k = k+step
        l = l+step
        summary = pipe(seg, max_length=max_summary_length, min_length=10, do_sample=False)
        output = output+summary[0]['summary_text']

    if(style=="BullPt"):
      output=("\n \u2022".join(output.split('.')))
      output=output[0:len(output)-1]
      output="\u2022"+ output + "\n\n"
    else:
      c=0
      list=output.split('.')
      for i in list:
        output+=i
        c+=1
        if(c==5):
          output+=" \n \n "
          c=0
    return output



