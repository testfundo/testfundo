import json
import requests
import time
import urllib




TOKEN ="407081358:AAF142Ha6KM_rqsOgJ48Icns4U2b2g2cNlc"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def ozone():
    menuboard = {'keyboard':[['Define'],['contributors'],['How do I help?'],]  ,'one_time_keyboard':True }
    reply_markup = {"keyboard":menuboard, "one_time_keyboard": True}
    return json.dumps(menuboard)
def global_key():
    keymenu = {'keyboard':[['What it means?'],['Reasons'],['How to control?']]  ,'one_time_keyboard':True }
    reply_markup = {"keyboard":keymenu, "one_time_keyboard": True}
    return json.dumps(keymenu)
    
def minikeyboard():
    #keyboard = [[item] for item in items]
    keymenu = {'keyboard':[['What is it?'],['causes'],['How can I help?']]  ,'one_time_keyboard':True }
    reply_markup = {"keyboard":keymenu, "one_time_keyboard": True}
    return json.dumps(keymenu)

def build_keyboard():
    
    keyboard = {'keyboard':[['Pollution'],['Global Warming'],['Ozone Depletion']]  , 'one_time_keyboard':True }
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(keyboard)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        if text =="/start":
            send_message("Press /done for the keyboard.Press /done at any case to come back to the main menu",chat)
        elif text == "/done":
            keyboar = build_keyboard()
            send_message("Choose an Option", chat, keyboar)
        elif text =="Pollution":
            menu = minikeyboard()
            send_message("*Select an option to continue*",chat,menu)
        elif text == "What is it?":
            send_message("Pollution occurs in different forms; air, water, soil, radioactive, noise, heat/ thermal and light. Every form of pollution has two sources of occurrence; the point and the non-point sources" + '.\n' + " The point sources are easy to identify, monitor and control, whereas the non-point sources are hard to control.  ",chat) 
        elif text == "causes":
            send_message("1.EFFLUENTS ->eg)industrial effluents \n 2.EMISSIONS ->eg) Vehicular emissions \n 3.WASTES -> eg) Industrial,Civic,E-wastes",chat)
        elif text == "How can I help?":
            contrib="Efforts are required to be made by each individual to control pollution. These efforts include -\n(a) Installation of proper sewage disposal methods.\n(b) Dumping of non biodegradable wastes in low lying areas.\n(c) Installation of gobar gas plants in areas of high availability of cow dung.\n(d) Reduction of smoke emission and treatment of chimney smoke to remove solid carbon particles.\n(e) Judicious use of fertilisers, pesticides and detergents (Detergents of low- level phosphate content are less harmful).\n(f) Growing plants like Pyrus (apple), Pinus (chir) and Vitis (grapes) is advo­cated because of their capability of metabolizing gaseous nitrogenous pollutants like nitrogen dioxide etc. and plants like coleus, ficus (banyan) can fix Carbon monoxide."
            send_message(contrib,chat) 
        elif text =="Global Warming":
            board = global_key()
            send_message("Choose an option",chat,board)
        elif text =="Ozone Depletion":
            palette = ozone()
            send_message("Choose an option",chat,palette)
        elif text =="What it means?":
            define ="Global warming is the current increase in temperature of the Earth's surface (both land and water) as well as it's atmosphere. Average temperatures around the world have risen by 0.75°C (1.4°F) over the last 100 years about two thirds of this increase has occurred since 1975.\n In the past, when the Earth experienced increases in temperature it was the result of natural causes but today it is being caused by the accumulation of greenhouse gases in the atmosphere produced by human activities."
            send_message(define,chat)
        elif text =="Reasons":
            rea="Greenhouse gas emissions and the enhanced greenhouse effect\nDeforestation\n Burning of fossil fuels\n"
            send_message(rea,chat)
        elif text == "How to control?":
            prev ="The car you drive: the most important personal climate decision.\nMake your house more air tight.\nBuy and USE a programmable thermostat\nUse power strips in your home office and home entertainment center\nUpgrade your refrigerator and air conditioner, especially if they are more than five years old\n"
            send_message(prev,chat)
        elif text == "Define":
            mean="The ozone layer is a belt of the naturally occurring gas ozone.\n It sits 9.3 to 18.6 miles (15 to 30 kilometers) above Earth, and serves as a shield from the harmful ultraviolet B (UVB) radiation emitted by the sun.\nToday, there is widespread concern that the ozone layer is deteriorating due to the release of pollution containing the chemicals chlorine and bromine. Such deterioration allows large amounts of ultraviolet B rays to reach Earth, which can cause skin cancer and cataracts in humans and harm animals as well."
            send_message(mean,chat)
        elif text == "contributors":
            contribu="1.Chlorofluorocarbons (CFCs), chemicals found mainly in spray aerosols heavily used by industrialized nations for much of the past 50 years, are the primary culprits in ozone layer breakdown. \nHydro chlorofluorocarbons (HCFCs) and volatile organic compounds (VOCs). Such substances are found in vehicular emissions, by-products of industrial processes, aerosols and refrigerants. All these ozone depleting substances remain stable in the lower atmospheric region, but as they reach the stratosphere, they get exposed to the ultra violet rays. This leads to their breakdown and releasing of free chlorine atoms which reacts with the ozone gas, thus leading to the depletion of the ozone layer."
            send_message(contribu,chat)
        elif text =="How do I help?":
            helper = "1. Limit private vehicle driving\n2. Use eco-friendly household cleaning products\n3. Avoid using pesticides\n4. Developing stringent regulations for rocket launches\n5. Banning the use of dangerous nitrous oxide"
            send_message(helper,chat)
        elif text =="/help":
            send_message("*Press /start to start the bot \nPress /done and press any key to explore_*",chat)
            
        else:
            send_message("I am sorry..I dont' get it..Press /help or/done",chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text,chat_id)


def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
     main()
