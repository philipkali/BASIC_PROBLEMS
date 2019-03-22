You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

For 4 or more names, the number in and 2 others simply increases.

=========================================================================================

=============================================================
//TEST CASES;
=============================================================
Test Cases:
describe('static tests', function() {
  it('should return correct text', function() {
    Test.assertEquals(likes([]), 'no one likes this');
    Test.assertEquals(likes(['Peter']), 'Peter likes this');
    Test.assertEquals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this');
    Test.assertEquals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this');
    Test.assertEquals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this');
  });
});

describe('random tests', function() {
  var names = [], sample;
  while (names.length < 100) names.push(Test.randomToken());

  it('should return correct text for 1 name', function() {
    sample = Test.randomize(names).slice(0, 1);
    Test.assertEquals(likes(sample.slice()), sample[0] + ' likes this');
  });
  
  it('should return correct text for 2 names', function() {
    sample = Test.randomize(names).slice(0, 2);
    Test.assertEquals(likes(sample.slice()), sample[0] + ' and ' + sample[1] + ' like this');
  });
  
  it('should return correct text for 3 names', function() {
    sample = Test.randomize(names).slice(0, 3);
    Test.assertEquals(likes(sample.slice()), sample[0] + ', ' + sample[1] + ' and ' + sample[2] + ' like this');
  });
  
  it('should return correct text for 4 or more names', function() {
    // 4 names
    sample = Test.randomize(names).slice(0, 4);
    Test.assertEquals(likes(sample.slice()), sample[0] + ', ' + sample[1] + ' and 2 others like this');
    
    // random number of names
    sample = Test.randomize(names).slice(0, Math.max(5, Math.min(99, Test.randomNumber())));
    Test.assertEquals(likes(sample.slice()), sample[0] + ', ' + sample[1] + ' and ' + (sample.length - 2) + ' others like this');
    
    // 100 names
    sample = Test.randomize(names);
    Test.assertEquals(likes(sample.slice()), sample[0] + ', ' + sample[1] + ' and 98 others like this');
  });
});



=======================================================================================




=============================================================
//ANSWER VARIATIONS;
=============================================================



function likes(names) {
  names = names || [];
  switch(names.length){
    case 0: return 'no one likes this'; break;
    case 1: return names[0] + ' likes this'; break;
    case 2: return names[0] + ' and ' + names[1] + ' like this'; break;
    case 3: return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'; break;
    default: return names[0] + ', ' + names[1] + ' and ' + (names.length - 2) + ' others like this';
  }
}

====================================================


function likes (names) {
  var templates = [
    'no one likes this',
    '{name} likes this',
    '{name} and {name} like this',
    '{name}, {name} and {name} like this',
    '{name}, {name} and {n} others like this'
  ];
  var idx = Math.min(names.length, 4);
  
  return templates[idx].replace(/{name}|{n}/g, function (val) {
    return val === '{name}' ? names.shift() : names.length;
  });
}


====================================================


function likes(names) {
  return {
    0: 'no one likes this',
    1: `${names[0]} likes this`, 
    2: `${names[0]} and ${names[1]} like this`, 
    3: `${names[0]}, ${names[1]} and ${names[2]} like this`, 
    4: `${names[0]}, ${names[1]} and ${names.length - 2} others like this`, 
  }[Math.min(4, names.length)]
}


====================================================


function likes(names) {
  if(names.length === 0) return "no one likes this";
  if(names.length === 1) return names[0] + " likes this";
  if(names.length === 2) return names[0] + " and " + names[1] + " like this";
  if(names.length === 3) return names[0] + ", " + names[1] + " and " + names[2] + " like this";
  return names[0] + ", " + names[1] + " and " + (names.length - 2) + " others like this";
}


====================================================


function likes(names) {
  switch(names.length){
    case 0:
      return "no one likes this";
    case 1:
      return names[0] + " likes this";
    case 2:
      return names[0] + " and " + names[1] + " like this";
    case 3:
      return names[0] + ", " + names[1] + " and " + names[2] + " like this";
    default: 
      return names[0] + ", " + names[1] + " and " + (names.length-2) + " others like this";
  }
}



====================================================



function likes(names) {
  names.length === 0 && (names = ["no one"]);
  let [a, b, c, ...others] = names;
  switch (names.length) {
    case 1: return `${a} likes this`;
    case 2: return `${a} and ${b} like this`;
    case 3: return `${a}, ${b} and ${c} like this`;
    default: return `${a}, ${b} and ${others.length + 1} others like this`;
  }
}






====================================================



function likes(peopleNames) {
  var feels = new FeelingsParty('like', 'this');
  for(var name in peopleNames) feels.addFeeler(new Person(peopleNames[name]));
  return feels.shareTheseFeelings();
}

function Person(name) {
 this.name = name;
}

Person.prototype.getName = function() {
  return this.name;
}

function FeelingsParty(emotion, target) {
 this.emotionalContext = emotion;
 this.emotionalSubject = target;
 this.peopleFeelingThisWay = [];
 this.numPeopleFeelingThisWay = 0;
}

FeelingsParty.prototype.getEmotionalContext = function() {
 return this.type;
}

FeelingsParty.prototype.addFeeler = function(person) {
    this.numPeopleFeelingThisWay++;
    this.peopleFeelingThisWay.push(person);
}

FeelingsParty.prototype.shareTheseFeelings = function() {
    this.findTheRightWords();
    if(this.numPeopleFeelingThisWay == 0) return 'no one ' + this.emotionalContext + ' ' + this.emotionalSubject;
    if(this.numPeopleFeelingThisWay == 1) return '' + this.peopleFeelingThisWay[0].getName() + ' ' + this.emotionalContext + ' ' + this.emotionalSubject;
    if(this.numPeopleFeelingThisWay == 2) return '' + this.peopleFeelingThisWay[0].getName() + ' and ' + this.peopleFeelingThisWay[1].getName() + ' ' + this.emotionalContext +  ' ' + this.emotionalSubject;
    if(this.numPeopleFeelingThisWay == 3) return '' + this.peopleFeelingThisWay[0].getName() + ', ' + this.peopleFeelingThisWay[1].getName() + ' and ' + this.peopleFeelingThisWay[2].getName() + ' ' + this.emotionalContext +  ' ' + this.emotionalSubject;
    return '' + this.peopleFeelingThisWay[0].getName() + ', ' + this.peopleFeelingThisWay[1].getName() + ' and ' + (this.numPeopleFeelingThisWay - 2) + ' others ' + this.emotionalContext + ' ' + this.emotionalSubject;
}

FeelingsParty.prototype.findTheRightWords = function() {
    if(this.numPeopleFeelingThisWay == 0 || this.numPeopleFeelingThisWay == 1) this.emotionalContext += 's';
}




===========================================================

function likes(names) {
  switch(names.length){
    case 0:
      return `no one likes this`;
    case 1: 
      return `${names[0]} likes this`;
    case 2: 
      return `${names[0]} and ${names[1]} like this`;
    case 3: 
      return `${names[0]}, ${names[1]} and ${names[2]} like this`;
    default: 
      return `${names[0]}, ${names[1]} and ${names.length - 2} others like this`;
  }
}



=============================================================

function likes (names) {
  var format = {
    0: "no one likes this",
    1: "{0} likes this",
    2: "{0} and {1} like this",
    3: "{0}, {1} and {2} like this"
  }[names.length] || "{0}, {1} and {n} others like this";
  
  return format.replace(/{([\dn])}/g, function (_, n) {
    return n == 'n' ? names.splice(2).length : names[parseInt(n, 10)];
  });
}


=============================================================

function likes(names) {
  var result = {
    0: ["no one likes this"],
    1: [ names[0], " likes this"],
    2: [ names[0], " and ", names[1] , " like this"],
    3: [ names[0], ", ", names[1],  " and ", names[2], " like this"],
    4: [ names[0], ", ", names[1], " and ", (names.length - 2) , " others like this"]
  }
  return names.length < 4 ? result[names.length].join("") : result[4].join("");
}

=============================================================









======================================
//My uploaded answer;
======================================

function likes(names) {
  // TODO
  if (names.length < 1) { //names.length === [] or === undefined returns undefined.
      return "no one likes this";
  } else if(names.length === 1) {
      return names[0] + " likes this";
  } else if(names.length === 2) {
      return names[0] + " and " + names[1]+ " like this";
  } else if(names.length === 3) {
      return names[0] + ", " + names[1] + " and " + names[2] + " like this";
  } else {
          if (names.length > 3){
              return names[0] + ", " + names[1] + " and " + (names.length - 2) + " others like this"
          }
    }
}

































