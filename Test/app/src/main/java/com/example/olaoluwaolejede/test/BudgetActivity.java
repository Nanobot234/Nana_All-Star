package com.example.olaoluwaolejede.test;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;


public class BudgetActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_budget);


    final Button forBtn = (Button) findViewById(R.id.But2);
        forBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick (View view){
            //contBtn.setText("Clicked");
                Intent intent = new Intent(BudgetActivity.this, FoodPlaceActivity.class);
                BudgetActivity.this.startActivity(intent);

            }

        });

    }
}









