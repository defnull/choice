%rebase html title=game.title
<div id='scene'>
    <div class='plot'>
        {{!game.get_html()}}
    </div>
    %if game.get_choices():
    <ol class='choices'>
        % for i, choice in game.get_choices():
        <li>
            <a href='?choice={{i}}'>{{choice}}</a>
        </li>
        % end
    </ol>
    %else:
    <b>Game Over!<b>
    %end
</div>
