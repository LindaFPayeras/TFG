package com.lily.front;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.lily.front.network.ApiService;
import com.lily.front.network.RetrofitClient;
import com.lily.front.network.models.ChatRequest;
import com.lily.front.network.models.ChatResponse;
import com.lily.front.network.models.Message;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class fragmentChat extends Fragment {

    private Button sendButton;
    private EditText messageEditText;
    private RecyclerView recyclerView;
    private MessageAdapter messageAdapter;
    private List<Message> messageList;

    private ApiService apiService;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_chat, container, false);

        apiService = RetrofitClient.getClient().create(ApiService.class);

        Log.d("CHAT", "apiService inicializado? " + (apiService != null));

        // Vistas
        sendButton = view.findViewById(R.id.btn_send);
        messageEditText = view.findViewById(R.id.et_message);
        recyclerView = view.findViewById(R.id.rv_messages);

        // RecyclerView
        messageList = new ArrayList<>();
        messageAdapter = new MessageAdapter(messageList);

        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        recyclerView.setAdapter(messageAdapter);

        // Botón
        sendButton.setOnClickListener(v -> sendMessage());

        return view;
    }

    private void sendMessage() {
        String messageText = messageEditText.getText().toString().trim();

        if (messageText.isEmpty()) return;

        // Mensaje usuario
        Message userMessage = new Message(messageText, "user");
        messageList.add(userMessage);
        messageAdapter.notifyItemInserted(messageList.size() - 1);

        messageEditText.setText("");

        String userId = "1";

        ChatRequest request = new ChatRequest(userId, messageText, "00.30");

        Log.d("CHAT", "Enviando: " + messageText);
        Log.d("CHAT", "apiService null? " + (apiService == null));

        apiService.sendMessage(request).enqueue(new Callback<ChatResponse>() {

            @Override
            public void onResponse(Call<ChatResponse> call, Response<ChatResponse> response) {

                Log.d("CHAT", "Respuesta recibida");

                if (response.isSuccessful() && response.body() != null) {

                    String botReply = response.body().getResponse();

                    Log.d("CHAT", "Bot: " + botReply);

                    Message botMessage = new Message(botReply, "bot");

                    messageList.add(botMessage);
                    messageAdapter.notifyItemInserted(messageList.size() - 1);
                } else {
                    Log.e("CHAT", "Respuesta no válida");
                }
            }

            @Override
            public void onFailure(Call<ChatResponse> call, Throwable t) {
                Log.e("CHAT", "Error: " + t.getMessage());
            }
        });
    }
}