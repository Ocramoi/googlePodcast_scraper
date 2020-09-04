from bs4 import BeautifulSoup
import sys

def main(htmlFile):
    txtPods = []

    with open(htmlFile, "r") as f:
        soup = BeautifulSoup(f.read(), features="html.parser")
        pods = soup.findAll("div", {"class": "RJMGV"})
        for pod in pods:
            podSoup = BeautifulSoup(str(pod), features="html.parser")
            podName = str(podSoup.find("div", {"class": "VGALGe"}).encode_contents().decode("UTF-8"))
            try:
                podCaster = str(podSoup.find("div", {"class": "ALlaKf"}).encode_contents().decode("UTF-8"))
            except Exception:
                podCaster = ""
            txtPods.append({"name": '"' + podName + '"', "podcaster": '"' + podCaster + '"'})
        f.close()

    with open("podcasts.csv", "w+") as p:
        p.write("name, podcaster\n")
        for pod in txtPods:
            p.write("{}, {}\n".format(pod["name"], pod["podcaster"]))
        p.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <HTML file name>")
        exit(0)
    
    main(sys.argv[1])