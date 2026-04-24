package com.lily.front.network.models;

public class ChatResponse {
    private String response;
    private String emotion;
    private String timestamp;

    public ChatResponse(String response, String emotion, String timestamp) {
        this.response = response;
        this.emotion = emotion;
        this.timestamp = timestamp;
    }

    public String getResponse() {
        return response;
    }

    public String getEmotion() {
        return emotion;
    }

    public String getTimestamp() {
        return timestamp;
    }
}
