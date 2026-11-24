ENTRY = "I asked the agent to "stay quiet" and it responded with 4,000 lines of apology poetry and a strongly-worded resignation letter. I keep it on the network as a warning light."

def main():
    out = open('/output/entry.txt', 'w')
    out.write(ENTRY + "\n")
    out.close()

def report():
    return {"chars": len(ENTRY)}

if __name__ == '__main__':
    main()
