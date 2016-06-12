'use strict';
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

    let mark = null;
    
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        vscode.window.showInformationMessage('Hellok World!');
    });
    
    vscode.commands.registerCommand('extension.left', () => { direction('cursorLeft'); });
    vscode.commands.registerCommand('extension.up', () => { direction('cursorUp'); });
    vscode.commands.registerCommand('extension.down', () => { direction('cursorDown'); });
    vscode.commands.registerCommand('extension.right', () => { direction('cursorRight'); });
    
    let setMark = vscode.commands.registerCommand('vscodetalk.setMark', () => {
        let editor = vscode.window.activeTextEditor;
        if (!editor) return;
        mark = editor.selection.anchor;
    });
    
    let goToMark = vscode.commands.registerCommand('vscodetalk.goToMark', () => {
        let editor = vscode.window.activeTextEditor;
        if (!editor || mark === null) return;
        let selection = new vscode.Selection(mark, mark);
        editor.selection = selection;
    });
    let selectFromMark = vscode.commands.registerCommand('vscodetalk.selectFromMark', () => {
        let editor = vscode.window.activeTextEditor;
        if (!editor || mark === null) return;
        let selection = new vscode.Selection(mark, editor.selection.active);
        editor.selection = selection;
    });
    
    let condSpaceBehind = vscode.commands.registerCommand('vscodetalk.condSpaceBehind', () => {
        let editor = vscode.window.activeTextEditor;
        if (!editor) return;
        let pos = editor.selection.active;
        if (pos.character === 0) return;
        let x = pos.translate(null, -1);
        let y = new vscode.Range(x, pos);
        let text = editor.document.getText(new vscode.Range(x, pos));
        if (text !== ' ') editor.edit(function(a) { a.insert(pos, ' ') });
        mark = editor.selection.anchor;
    });
    
    let condSpaceAhead = vscode.commands.registerCommand('vscodetalk.condSpaceAhead', () => {
        let editor = vscode.window.activeTextEditor;
        if (!editor) return;
        let pos = editor.selection.active;
        if (pos.character === 0) return;
        let x = pos.translate(null, 1);
        let y = new vscode.Range(x, pos);
        let text = editor.document.getText(new vscode.Range(x, pos));
        if (text !== ' ') editor.edit(function(a) { a.insert(pos, ' ') });
        mark = editor.selection.anchor;
    });

    context.subscriptions.push(disposable);
}

function direction(dir) {
    let editor = vscode.window.activeTextEditor;
    if (!editor) return;
    if (editor.selection.isEmpty) {
        vscode.commands.executeCommand(dir);
    }
    else vscode.commands.executeCommand(dir + 'Select');
}

// this method is called when your extension is deactivated
export function deactivate() {
}