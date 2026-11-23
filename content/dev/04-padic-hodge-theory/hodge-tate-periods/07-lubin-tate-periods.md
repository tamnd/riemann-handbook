---
title: Lubin-Tate periods
decls:
  - PositivityTheory.SecR.Hladr2.pre_period
  - PositivityTheory.SecR.Hladr2.hasPeriods_main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lubin-Tate periods

This section and the next one turn to the second subject of the chapter: the $l$-adic character of an algebraic Hecke character is de Rham, with the expected Hodge-Tate jumps. The local input is a period in $B_{\mathrm{dR}}$ for each embedding of a Lubin-Tate character. Let $K$ be a finite extension of $\mathbb{Q}_l$ and $\chi$ a Lubin-Tate character of $G_K$. For each embedding $\mu$ of $K$ we build a nonzero element $y_\mu$ of $B_{\mathrm{dR}}$ on which $G_K$ acts through $\mu \circ \chi$. Its filtration degree is exactly $1$ if $\mu$ is the inclusion and exactly $0$ otherwise. The construction is the classical one: a compatible system of torsion points of the [[Lubin-Tate formal group laws|77QT4B80V8]] in the tilt gives an element $Q$ of $B_{\mathrm{dR}}^+$, and the period is the limit of $\pi^{-n}[\pi^n](Q)$. The two theorems here are used in [the theorem on de Rham Hecke characters](/entry/field-of-leaves/) of the next section.

Throughout, $l$ is a prime, $\bar{\mathbb{Q}}_l$ is an algebraic closure of $\mathbb{Q}_l$, $\mathbb{C}_l$ is its completion and $G_{\mathbb{Q}_l} = \mathrm{Gal}(\bar{\mathbb{Q}}_l/\mathbb{Q}_l)$. A finite extension $K$ of $\mathbb{Q}_l$ is a subfield of $\bar{\mathbb{Q}}_l$, with ring of integers $O_K$ and Galois group $G_K \subseteq G_{\mathbb{Q}_l}$. An embedding of $K$ is a $\mathbb{Q}_l$-algebra map $\mu : K \to \bar{\mathbb{Q}}_l$, and $\mathrm{id}$ is the inclusion. We use the [period rings](/learn/galois-representations/#period-rings) of the Background ([[Fontaine's period rings|K6HW8YWCQJ]]): the tilt $\mathcal{O}^\flat$ of $\mathcal{O}_{\mathbb{C}_l}$, the Teichmüller lift $[x] \in B_{\mathrm{dR}}^+$ of $x \in \mathcal{O}^\flat$, the map $\theta : B_{\mathrm{dR}}^+ \to \mathbb{C}_l$, the filtration $\mathrm{Fil}^k = (\ker\theta)^k$ of $B_{\mathrm{dR}}^+$, and the inclusion $\bar{\mathbb{Q}}_l \subseteq B_{\mathrm{dR}}^+$. The group $G_{\mathbb{Q}_l}$ acts on $\mathcal{O}^\flat$ and on $B_{\mathrm{dR}}^+$, and these actions commute with $\theta$ and with $x \mapsto [x]$. We have $\theta([x]) = x^\sharp$. For $\pi \in O_K$ put $q = \#(O_K/\pi)$ and $f_\pi(X) = \pi X + X^q$.

### Lubin-Tate characters

**Definition 4.7.1 (Lubin-Tate datum).** Let $\chi : G_K \to K^\times$ be a homomorphism. A *Lubin-Tate datum* for $\chi$ is a pair of an irreducible element $\pi$ of $O_K$ and a sequence $z_0, z_1, \dots$ in $\bar{\mathbb{Q}}_l$ such that:

1. $z_0 = 0$ and $z_1 \neq 0$;
2. $z_{n+1}^q + \pi z_{n+1} = z_n$ for all $n$;
3. for each $g \in G_K$, each power series $\varphi \in O_K[[X]]$ with $\varphi(0) = 0$, $\varphi'(0) = \chi(g)$ and $\varphi \circ f_\pi = f_\pi \circ \varphi$, and each $n$, the series $\sum_k \varphi_k z_n^k$ converges in $\bar{\mathbb{Q}}_l$ to $g(z_n)$.

The character $\chi$ is a *Lubin-Tate character* if it has a Lubin-Tate datum.

Here $\pi$ is a uniformizer of $K$ and $f_\pi$ is a Lubin-Tate series for $\pi$. Condition 2 says $f_\pi(z_{n+1}) = z_n$, so $z_n$ is a compatible system of torsion points of the Lubin-Tate group $F_\pi$ with $z_1 \neq 0$. For $a \in O_K$ there is exactly one power series $[a]_\pi$ with $[a]_\pi(0) = 0$, linear term $a$ and $[a]_\pi \circ f_\pi = f_\pi \circ [a]_\pi$. So condition 3 says $g(z_n) = [\chi(g)]_\pi(z_n)$. This is the Galois action on the torsion of $F_\pi$ (Lubin and Tate). By [local class field theory](/learn/class-field-theory/#local-class-field-theory) ([[local class field theory|SHEN158T3M]]), the Lubin-Tate character of $\pi$ factors through the abelianization of $G_K$. If the reciprocity map $\mathrm{rec}_K$ sends $\pi$ to an arithmetic Frobenius that fixes all $z_n$, then $\chi(\mathrm{rec}_K(u)) = u^{-1}$ for $u \in O_K^\times$.

### Pre-periods

**Definition 4.7.2 (Pre-period).** Let $\chi : G_K \to K^\times$ be a homomorphism and $\mu$ an embedding of $K$. A *pre-period* of $\chi$ at $\mu$ is an element $t \in B_{\mathrm{dR}}^+$ such that:

1. $t \neq 0$;
2. $g(t) = \mu(\chi(g))\, t$ for each $g \in G_K$ that fixes $\mu(K)$ pointwise;
3. if $\mu = \mathrm{id}$, then $\theta(t) = 0$.

For $K = \mathbb{Q}_l$ and $\chi$ the [[cyclotomic character|XSGB5K2KEG]], the element $t = \log[\varepsilon]$ is a pre-period at $\mathrm{id}$. In general we construct a pre-period from a torsion system in the tilt. We state the existence of such a system as a condition.

**Definition 4.7.3 (Tilt condition).** The *tilt condition* holds if for each prime $l$, each $K$, each homomorphism $\chi : G_K \to K^\times$ with a Lubin-Tate datum $(\pi, z)$, and each embedding $\mu$ of $K$, there are a ring map $r : O_K \to \mathcal{O}^\flat$ and elements $v_0, v_1, \dots$ of $\mathcal{O}^\flat$ with:

1. $v_{n+1}^q = v_n$ for all $n$, $v_0 \neq 0$ and $|v_0^\sharp| < 1$;
2. for each $c \in O_K$ there is $c' \in O_K$ with $[r(c)] = \mu(c + \pi c')$;
3. for each $g \in G_K$ and each $\varphi$ as in condition 3 of a Lubin-Tate datum, $v_n^D$ divides $g(v_n) - \sum_{i < D} r(\varphi_i)\, v_n^i$ in $\mathcal{O}^\flat$ for all $n$ and $D$;
4. if $\mu = \mathrm{id}$, then $|v_n^\sharp - z_n| \leq |\pi|$ for all $n$.

Condition 3 says that $g(v_n) = (r\varphi)(v_n)$ in $\mathcal{O}^\flat$, so $v_n$ is a torsion system for the reduction of $f_\pi$. Condition 4 says that $v_n$ lifts $z_n$ modulo $\pi$.

**Theorem 4.7.4 (Pre-periods of Lubin-Tate characters).** Assume the tilt condition. Let $\chi : G_K \to K^\times$ be a homomorphism with a Lubin-Tate datum $(\pi, z)$, and assume that $\chi$ is continuous as a map to $\bar{\mathbb{Q}}_l$. Then for each embedding $\mu$ of $K$ there is a pre-period of $\chi$ at $\mu$.

Lean: `PositivityTheory.SecR.Hladr2.pre_period`.

*Proof.* Since $\pi$ is irreducible, $q \geq 2$, $l$ divides $q$, $\pi$ divides $l$, and $|\mu(\pi)| < 1$. Let $K'$ be the normal closure of $K$ in $\bar{\mathbb{Q}}_l$. There is a subring $S$ of $B_{\mathrm{dR}}^+$ that contains the image of $A_{\mathrm{inf}}$ and the integers of $K'$, is stable under $G_{\mathbb{Q}_l}$, and has $|\theta(s)| \leq 1$ for $s \in S$. For each nonzero integer $x$ of $K'$ with $|x| < 1$, the lattice $S$ has two properties with respect to $\varpi = x$. First, $\varpi$ is a unit of $B_{\mathrm{dR}}^+$, the sums $\sum_n \varpi^n s_n$ with $s_n \in S$ converge in $S$, the filtration $\mathrm{Fil}^k$ is separated and complete, and $S$ is closed for the sets $\varpi^m S + \mathrm{Fil}^k$. Second, no nonzero Teichmüller element $[u]$ lies in $\varpi S$.

Take $\varpi = \mu(\pi)$, with inverse $\varpi'$ in $B_{\mathrm{dR}}^+$, and let $r$ and $v_n$ be given by the tilt condition. Then $q \in \varpi S$, and $[v_{n+1}]^q = [v_n]$ with $[v_n] \in S$. Write $f(X) = \varpi X + X^q$ and $f^n$ for its $n$-th iterate.

First, the limit of the torsion system. There is $Q \in S$ with $Q - f^n([v_n]) \in \varpi^{n+1} S$ for all $n$. Since $|v_0^\sharp| < 1$, a power $[v_0]^M$ with $M > 0$ lies in $\varpi S + \mathrm{Fil}^1$, and so does $Q^M$.

Second, the period. The sequence $\varpi'^n f^n(Q)$ converges to an element $t$ of $B_{\mathrm{dR}}^+$, in the topology defined by the sets $\varpi^m S + \mathrm{Fil}^k$. Classically, $t$ is $\log_{F}(Q)$ for the logarithm of the Lubin-Tate group.

Third, $t \neq 0$. If $t = 0$, then $f^n(Q) = 0$ for some $n$. By induction on $n$, $f^n(Q) - [v_0]^{q^n} \in \varpi S$, so $[v_0^{q^n}] \in \varpi S$. This is false, since $v_0 \neq 0$.

Fourth, the Galois action. Let $g \in G_K$ fix $\mu(K)$. Since $\chi$ is continuous and $G_K$ is compact, $\chi(g) \in O_K$. Let $\varphi = [\chi(g)]_\pi$. Then $g(\varpi) = \varpi$. By condition 3 of the tilt condition and condition 2 for $r$, the series $\mu\varphi$ evaluated at $[v_n]$ agrees with $g([v_n])$ modulo $\varpi S + \mathrm{Fil}^k$ for each $k$. Since $\mu\varphi$ commutes with $f$, this passes to $Q$ at every level: $\mu\varphi(Q)$ agrees with $g(Q)$ modulo $\varpi^m S + \mathrm{Fil}^k$ for all $m$ and $k$. Then $g(t) = \lim \varpi'^n f^n(g Q)$, and the linear term of $\mu\varphi$ gives $g(t) = \mu(\varphi'(0))\, t = \mu(\chi(g))\, t$.

Fifth, $\theta(t)$ for $\mu = \mathrm{id}$. Then $\theta(\varpi) = \pi$, and the numbers $\theta([v_n])$ and $z_n$ differ by at most $|\pi|$ by condition 4. The $z_n$ satisfy $z_{n+1}^q + \pi z_{n+1} = z_n$ with $z_0 = 0$. From these facts and $|q| \leq |\pi|$ we get $\theta(Q) = 0$. Since $\theta$ kills $Q$, it kills each $f^n(Q)$ and the limit $t$. $\square$

### Periods

The ring $B_{\mathrm{dR}}$ appears in the de Rham theory of the development through a *period datum* $P$ at $l$: a ring $B_P$ with an action of $G_{\mathbb{Q}_l}$, a map $\bar{\mathbb{Q}}_l \to B_P$, and for each $K$ a filtration $\mathrm{Fil}^a_K$ of $B_P$ indexed by $a \in \mathbb{Z}$. A *tie* of $P$ is a ring isomorphism $e : B_P \to B_{\mathrm{dR}}$ that commutes with the action of $G_{\mathbb{Q}_l}$, carries $\mathrm{Fil}^a_K$ onto $\mathrm{Fil}^a B_{\mathrm{dR}}$ for all $K$ and $a$, and carries each $x \in \bar{\mathbb{Q}}_l$ to an element of $B_{\mathrm{dR}}^+$ with $\theta$-value $x$. A tie also compares a crystalline ring of $P$ with $B_{\mathrm{cris}}$, which we do not use. For the [de Rham representations](/learn/padic-hodge/#de-rham-representations) of the Background, $P$ with a tie is $B_{\mathrm{dR}}$ with its filtration.

**Definition 4.7.5 (Periods of a character).** Let $P$ be a period datum at $l$ and $\chi : G_K \to K^\times$ a homomorphism. Then $\chi$ *has periods in* $P$ if for each embedding $\mu$ of $K$ there is $y \in B_P$ such that:

1. $g(y) = \mu(\chi(g))\, y$ for each $g \in G_K$ that fixes $\mu(K)$ pointwise;
2. if $\mu = \mathrm{id}$, then $y \in \mathrm{Fil}^1_K \setminus \mathrm{Fil}^2_K$;
3. if $\mu \neq \mathrm{id}$, then $y \in \mathrm{Fil}^0_K \setminus \mathrm{Fil}^1_K$.

So a character with periods has Hodge-Tate weight $1$ at $\mathrm{id}$ and $0$ at the other embeddings, in the sense of the filtration degree of $y_\mu$. The lower bounds come from the pre-periods. The upper bounds need a second condition.

**Definition 4.7.6 (Product condition).** The *product condition* holds if for each prime $l$, each $K$ and each homomorphism $\chi : G_K \to K^\times$ with
$$N_{K/\mathbb{Q}_l}\bigl(\chi(g)\bigr) = \chi_{\mathrm{cyc}}(g) \quad \text{for each } g \in G_K \text{ that fixes } \mathbb{Q}_l^{\mathrm{ur}},$$
the following holds. If $t_\mu$ is a pre-period of $\chi$ at $\mu$ for each embedding $\mu$, then $t_{\mathrm{id}} \notin \mathrm{Fil}^2$, and $t_\mu \notin \mathrm{Fil}^1$ for $\mu \neq \mathrm{id}$. Here $\mathbb{Q}_l^{\mathrm{ur}} \subseteq \bar{\mathbb{Q}}_l$ is the maximal unramified extension.

The idea is that $\prod_\mu t_\mu$ is a period of $N_{K/\mathbb{Q}_l} \circ \chi$, which is the cyclotomic character up to an unramified character. Such a period has filtration degree exactly $1$. The degree of $t_{\mathrm{id}}$ is at least $1$, and the degrees add, so $t_{\mathrm{id}}$ has degree $1$ and the others have degree $0$.

**Theorem 4.7.7 (Periods of Lubin-Tate characters).** Assume the tilt condition and the product condition. Let $P$ be a period datum at $l$ that has a tie. Let $\chi : G_K \to K^\times$ be a Lubin-Tate character that is continuous as a map to $\bar{\mathbb{Q}}_l$. Then $\chi$ has periods in $P$.

Lean: `PositivityTheory.SecR.Hladr2.hasPeriods_main`.

*Proof.* Fix a tie $e$. A continuous Lubin-Tate character satisfies $N_{K/\mathbb{Q}_l}(\chi(g)) = \chi_{\mathrm{cyc}}(g)$ for each $g \in G_K$ that fixes $\mathbb{Q}_l^{\mathrm{ur}}$. This is a separate theorem of the development; classically it follows from the norm compatibility of the local reciprocity maps and from the case $K = \mathbb{Q}_l$, where the Lubin-Tate character of $l$ is the cyclotomic character. Let $(\pi, z)$ be a Lubin-Tate datum. By [the theorem on pre-periods](/entry/pre-period/), for each $\mu$ there is a pre-period $t_\mu$. By the product condition, $t_{\mathrm{id}} \notin \mathrm{Fil}^2$ and $t_\mu \notin \mathrm{Fil}^1$ for $\mu \neq \mathrm{id}$.

Fix $\mu$ and put $y = e^{-1}(t_\mu)$. Since $e$ carries $\mathrm{Fil}^n_K$ onto $\mathrm{Fil}^n B_{\mathrm{dR}}$, and $\mathrm{Fil}^n B_{\mathrm{dR}} \cap B_{\mathrm{dR}}^+ = (\ker\theta)^n$ for $n \geq 0$, we get $y \in \mathrm{Fil}^n_K$ if and only if $t_\mu \in (\ker\theta)^n$. A ring map $\bar{\mathbb{Q}}_l \to B_{\mathrm{dR}}^+$ that lifts $\theta$ is the inclusion, so $e$ restricts to the inclusion on $\bar{\mathbb{Q}}_l$. For $g \in G_K$ that fixes $\mu(K)$,
$$e(g y) = g(t_\mu) = \mu(\chi(g))\, t_\mu = e\bigl(\mu(\chi(g))\, y\bigr),$$
and $e$ is injective, so $g y = \mu(\chi(g))\, y$. If $\mu = \mathrm{id}$, then $\theta(t_\mu) = 0$, so $t_\mu \in \mathrm{Fil}^1$ and $y \in \mathrm{Fil}^1_K$; and $y \notin \mathrm{Fil}^2_K$ since $t_\mu \notin \mathrm{Fil}^2$. If $\mu \neq \mathrm{id}$, then $y \in \mathrm{Fil}^0_K$ since $(\ker\theta)^0$ is all of $B_{\mathrm{dR}}^+$, and $y \notin \mathrm{Fil}^1_K$ since $t_\mu \notin \mathrm{Fil}^1$. $\square$

**Remark 4.7.8 (Formalization).** The tilt condition and the product condition are propositions, `TiltLeaf` and `ProductLeaf` at [FieldOfLeaves.lean](lean:Development/WeilBound/CoreStatements/HeckeCharacterDeRham/DeRhamHeckeResults/LAdicHeckeDeRham/LAdicHeckeFields/FieldOfLeaves.lean#L30) and line 41, and both theorems take them as hypotheses. The caller at [Outright.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/HeckeLAdicCharacters/Outright.lean#L8) supplies them with `LTPer.Tilt.tilt_period` and `lubin_tate_period_not_filtered`; the second is again a second name, proved by `first | exact @...exact_degrees_of_product | ...`. The Lubin-Tate datum and the Lubin-Tate character are two definitions, `LTData` and `IsLTChar`, with the same five conditions written out twice. A period datum is `LocPrime`, and a tie is a term of the structure `LocTied6`. The filtration of a period datum is given for each $K$, but the tie makes it independent of $K$. The tie is only asked to send $x \in \bar{\mathbb{Q}}_l$ to some lift of $x$ in $B_{\mathrm{dR}}^+$; the proof of the second theorem deduces that this lift is the canonical one, and transfers the filtration by `fil_iff`. The steps of the first proof (the lattice, the limit of the torsion system, the convergence and the action on the limit) are separate theorems of the development, which the proof uses as given.
