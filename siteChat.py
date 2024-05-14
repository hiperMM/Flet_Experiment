import flet as ft

def main(page):
    chat = ft.Column()
    messageField = ft.TextField("type your message")

    title = ft.Text("First website")
    windowTitle = ft.Text("Welcome")
    userNameField = ft.TextField(label="Enter your name")

    def broadcast(message):
        chatText = ft.Text(message)
        chat.controls.append(chatText)
        print(message)
        page.update()

    page.pubsub.subscribe(broadcast)
    
    def SendMessage(event):
        messageText = messageField.value
        userName = userNameField.value
        message = f"{userName}: {messageText}"
        page.pubsub.send_all(message)
        
        messageField.value = ""
        print("send message")
        page.update()

    messageField = ft.TextField(label="Type your message", on_submit=SendMessage)
    sendMessageButton = ft.ElevatedButton("Send message", on_click=SendMessage)

    def StartChat(event):      
        page.dialog = dialog
        dialog.open = True
        page.update()

    messageRow = ft.Row([messageField, sendMessageButton])

    def EnterChat(event):
        page.remove(title)
        page.remove(startButton)
        dialog.open = False 
        page.add(chat)
        page.add(messageRow)
        message = f"{userNameField.value} entered the chat"
        page.pubsub.send_all(message)
        page.update()
        
    startButton = ft.ElevatedButton("Start chat", on_click=StartChat)
    enterChatButton = ft.ElevatedButton("Enter chat", on_click=EnterChat)

    dialog = ft.AlertDialog(
        title=windowTitle,
        content=userNameField,
        actions=[enterChatButton]
    )

    page.add(title)
    page.add(startButton)

ft.app(main, view=ft.WEB_BROWSER)
