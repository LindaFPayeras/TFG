package com.lily.front;

public class patientCard {
    private String nameSurname;
    private String lastMessage;
    private String lastEmotion;
    private int profilePicture;

    public patientCard(String nameSurname, String lastMessage, String lastEmotion
            //, int profilePicture
    ) {
        this.nameSurname = nameSurname;
        this.lastMessage = lastMessage;
        this.lastEmotion = lastEmotion;
        // this.profilePicture = profilePicture;
    }

    public String getNameSurname() {
        return nameSurname;
    }

    public void setNameSurname(String nameSurname) {
        this.nameSurname = nameSurname;
    }

    public String getLastMessage() {
        return lastMessage;
    }

    public void setLastMessage(String lastMessage) {
        this.lastMessage = lastMessage;
    }

    public String getLastEmotion() {
        return lastEmotion;
    }

    public void setLastEmotion(String lastEmotion) {
        this.lastEmotion = lastEmotion;
    }

//    public int getProfilePicture() {
//        return profilePicture;
//    }
//
//    public void setProfilePicture(int profilePicture) {
//        this.profilePicture = profilePicture;
//    }
}
