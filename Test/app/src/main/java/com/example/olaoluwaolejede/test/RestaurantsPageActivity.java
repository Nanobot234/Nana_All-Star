package com.example.olaoluwaolejede.test;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class RestaurantsPageActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_restaurants_page);

        final Button BigBtn = (Button) findViewById(R.id.But4);
/*
        BigBtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                //contBtn.setText("Clicked");
                Intent intent = new Intent(RestaurantsPageActivity.this, RestaurantsInfoActivity.class);
                RestaurantsPageActivity.this.startActivity(intent);
            }

        });
        */
        final TextView BigText = (TextView) findViewById(R.id.TextViewC);
        BigText.setOnClickListener(new View.OnClickListener(){
            public void onClick(View view) {
                Intent intent = new Intent(RestaurantsPageActivity.this, RestaurantsInfoActivity.class);
                startActivity(intent);

            }
        });


    }
}
