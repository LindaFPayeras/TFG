package com.lily.front;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.lily.front.network.models.Message;

import java.util.ArrayList;
import java.util.List;

public class fragmentChat extends Fragment {

    private Button sendButton;
    private EditText messageEditText;
    private RecyclerView recyclerView;
    private MessageAdapter messageAdapter;
    private List<Message> messageList;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_chat, container, false);

        // 1. Vincular vistas
        sendButton = view.findViewById(R.id.btn_send);
        messageEditText = view.findViewById(R.id.et_message);
        recyclerView = view.findViewById(R.id.rv_messages);

        // 2. Configurar RecyclerView
        messageList = new ArrayList<>();
        messageAdapter = new MessageAdapter(messageList);

        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        recyclerView.setAdapter(messageAdapter);

        // 3. Listener botón
        sendButton.setOnClickListener(v -> sendMessage());

        return view;
    }

    private void sendMessage() {
        String messageText = messageEditText.getText().toString().trim();

        if (messageText.isEmpty()) return;

        // Crear mensaje del usuario
        Message userMessage = new Message(messageText, "user");

        // Añadirlo a la lista
        messageList.add(userMessage);

        // Notificar al adapter
        messageAdapter.notifyItemInserted(messageList.size() - 1);

        // Limpiar el input
        messageEditText.setText("");
    }
}
