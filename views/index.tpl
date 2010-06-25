%rebase html title="Select a game"

<form method='POST'>
    <select name='game'>
        %for name, title in games.iteritems():
        <option value='{{name}}'>{{title}}</option>
        %end
    </select>
    <input type='submit' value='Start new game'/>
</form>