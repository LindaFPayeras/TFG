package com.lily.front.network;

import com.lily.front.network.models.ChatRequest;
import com.lily.front.network.models.ChatResponse;
import com.lily.front.network.models.LoginRequest;
import com.lily.front.network.models.LoginResponse;
import com.lily.front.network.models.Message;
import com.lily.front.network.models.SummaryResponse;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;

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