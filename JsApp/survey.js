import { StatusBar } from 'expo-status-bar';
import React, {useState} from 'react';
import {Text, TouchableWithoutFeedbackComponent, View, Image, TextInput, Button} from 'react-native';
import {gstyles} from '../styles';
import {TouchableWithoutFeedback} from "react-native";



export default function Survey() {
    const [text, setValue] = useState('');

    const OnChange = (text)=>{
        setValue(text);
    };

    return (
        <View style={gstyles.container}>
            <Text style={gstyles.question}>Сова/жаворонок?</Text>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Ответ'/>
            <Text style={gstyles.question}>Сколько времени нужен на отдых?</Text>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Ответ'/>
            <Text style={gstyles.question}>Как часто кушаете?</Text>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Ответ'/>
            <Text style={gstyles.question}>Насколько устаете?</Text>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Ответ'/>
            <Text style={gstyles.question}>Мера отвратительности</Text>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Ответ'/>
            <Text style={gstyles.question}>Вы гей?</Text>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Ответ'/>
            <Text style={gstyles.question}>Вы учитесь на факи?</Text>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Ответ'/>

        </View>
    );
}
