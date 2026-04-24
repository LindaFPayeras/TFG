package com.lily.front.network.models;

public class ChatRequest {
    private String user_id;
    private String message;
    private String timestamp;

    public ChatRequest(String user_id, String message, String timestamp) {
        this.user_id = user_id;
        this.message = message;
        this.timestamp = timestamp;
    }
}
