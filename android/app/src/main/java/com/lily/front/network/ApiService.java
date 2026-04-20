package com.lily.front.network;

import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;

public interface ApiService {

    @POST("login")
    Call<LoginResponse> login(@Body LoginRequest request);

    @POST("chat")
    Call<ChatResponse> sendMessage(@Body ChatRequest request);

    @GET("history/{user_id}")
    Call<List<Message>> getHistory(@Path("user_id") String userId);

    @GET("summary/{user_id}")
    Call<SummaryResponse> getSummary(@Path("user_id") String userId);
}