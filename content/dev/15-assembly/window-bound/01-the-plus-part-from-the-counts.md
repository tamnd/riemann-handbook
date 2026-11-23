---
title: The plus part from the counts
decls:
  - UpperTheory.V.HV.pointHV_of_counts
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The plus part from the counts

This section bounds the plus part of the Tate-Shafarevich lengths of the CM fields that occur in the window bound. The input is a set of six counts. Each count bounds one length attached to a [[Dirichlet character|JR4QSEFXWF]] and a prime $l$, in one case of a case split. The section proves a bound at one point, for one host and one length $t$. The next section moves the bound to a window of points and joins it with the bounds for the prime $2$ and for the minus part. That gives the statement VWin of the [proof chapter on VWin](/proof/vwin/).

We use the lengths of [the proof chapter](/proof/vwin/). Let $E$ be a number field, $l$ a prime, $k$ an integer, and fix the local data of that chapter: an algebraic closure of $E$, the set of places above $l$, and a character with values in $\mathbb{Z}_l^\times$ that restricts to the [[cyclotomic character|XSGB5K2KEG]]. Let $\text{Ш}_l(E, k)$ be the Tate-Shafarevich group of $\mathbb{Q}_l/\mathbb{Z}_l$ twisted by the $(-k)$-th power of this character, as in [the Background](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups). Let $\ell_l(E, k) \in \mathbb{N} \cup \{\infty\}$ be its [[length|CZSCNZH8VY]] over $\mathbb{Z}_l$.

**Definition 2.1.1 (Plus and minus parts).** Let $E$ be a CM field, $l$ an odd prime and $k \geq 1$. Complex conjugation acts on $\text{Ш}_l(E, k)$ with square $1$. The *plus part* $\text{Ш}^+_l(E, k)$ is the eigenspace for the eigenvalue $(-1)^k$, and the *minus part* $\text{Ш}^-_l(E, k)$ is the eigenspace for $(-1)^{k+1}$. Let $\ell^\pm_l(E, k)$ be their lengths. For $t \geq 1$ and $B \in \mathbb{R}$, we say that $E$ has *plus bound* $B$ *below* $t$ if for each choice of local data the lengths $\ell^+_l(E, k)$ are finite for all odd $l$ and $0 < k < t$, and

$$\sum_{l \in S} \log l \sum_{k=1}^{t-1} \ell^+_l(E, k) \leq B$$

for each finite set $S$ of odd primes. The *minus bound* is defined in the same way with $\ell^-$. For one prime $l$, we say that a number field $L$ has $l$-*bound* $B$ *below* $t$ if each $\ell_l(L, k)$ with $0 < k < t$ is finite and $\sum_{k=1}^{t-1} \ell_l(L, k) \leq B$.

Since $l$ is odd, $\text{Ш}_l(E, k)$ is the direct sum of its two parts, as in [the Background](/learn/galois-cohomology/#plus-and-minus-parts). So $\ell_l = \ell^+_l + \ell^-_l$.

**Definition 2.1.2 (Host).** A *host* is a tuple $h = (\psi, m, q, d)$ where $\psi$ is a primitive Dirichlet character of conductor $N_\psi$ and order $o_\psi$, $m \geq 2$ is an integer, $q$ is a prime with $q \equiv 3 \pmod 8$, $d$ is a prime with $d \equiv 7 \pmod{16}$, and $qd$ is prime to $N_\psi$. Its *modulus* is $N_h = \mathrm{lcm}(2^{m+2}, N_\psi) \, q d$. Let $H_h \subseteq (\mathbb{Z}/N_h)^\times$ be the subgroup of classes $a$ with $a \equiv \pm 1 \pmod{2^{m+2}}$, $\psi(a) = 1$, and $a$ a square modulo $q$ and modulo $d$. A *character of* $h$ is a Dirichlet character modulo $N_h$ that is trivial on $H_h$. For $k \in \mathbb{Z}$ let $X_h(k)$ be the set of characters $\phi$ of $h$ with $\phi(-1) = (-1)^k$.

Let $E_h$ be the fixed field of $H_h$ in the [[cyclotomic field|NN77VYSGXR]] $\mathbb{Q}(\zeta_{N_h})$. A field $E$ is a *field of* $h$ if it is isomorphic to $E_h$. This is the condition on $E$ in the statement VWin of [the proof chapter](/proof/vwin/), with $m = e(x)$. Complex conjugation on $E_h$ is the class of $-1$. Since $q \equiv 3 \pmod 4$, $-1$ is not a square modulo $q$, so $-1 \notin H_h$ and complex conjugation is not trivial on $E_h$. An abelian number field on which complex conjugation is not trivial is a CM field. So $E_h$ is a CM field.

**Definition 2.1.3 (Bad primes).** Let $\psi$ be a primitive character. Let $p_K$ be the least prime $p \equiv 3 \pmod 4$ with $p \geq 7$ and $p$ prime to $N_\psi$. Let $h^*$ be the class number of $\mathbb{Q}(\sqrt{-p_K})$. Let $p_1$ be the least prime that is $1$ modulo the odd part of $o_\psi$ and prime to $2 N_\psi p_K$. The set of *bad primes* $B_\psi$ is $\{3\}$ together with the odd prime factors of $o_\psi N_\psi p_K h^* p_1$.

A host $h$ is *large for* $t$ if $2t + 1 < q$, $2t + 1 < d$, and each of $N_\psi$, $o_\psi$, $p_K$, $h^*$, $p_1$ is less than $q$ and less than $d$. Then every bad prime is less than $q$ and $d$.

For an odd prime $l$, a finite extension $\mathcal{O}$ of $\mathbb{Z}_l$ with enough roots of unity, a character $\phi$ of $h$ and $k \geq 1$, the counts use a length $v_l(\phi, k) \in \mathbb{N} \cup \{\infty\}$ of an $\mathcal{O}$-module attached to $\phi$ and the $k$-th twist, and a real number $\nu_l(\phi, k) \geq 0$, its normalized size. We do not need their definitions. We only use the reduction lemma below, which links them to the plus part.

**Definition 2.1.4 (The cases).** Let $h$ be a host, $l$ an odd prime, $k \geq 1$ and $\phi$ a character of $h$. Let $\phi_l$ be the prime-to-$l$ part of $\phi$. The pair $(l, k, \phi)$ is in

- case I if $l \notin B_\psi$ and $l - 1 \nmid 2k$;
- case Z if $l \notin B_\psi$, $l - 1 \mid 2k$ and $\phi = 1$;
- case II if $k \geq 2$, an eigenvalue condition on $\phi$ at $l$ holds, and $l \in B_\psi$ or $l - 1 \mid 2k$;
- case III if $l \notin B_\psi$, $l - 1 \mid 2k$, $\phi \neq 1$ and $\phi$ has odd order;
- case IV if $l \in B_\psi$, $k \geq 2$ and $\phi_l$ has odd order;
- case V if $l \in B_\psi$ and $k = 1$.

Case V is split at a threshold: case V$_\leq$ if $R_1 \leq 2^{c_2(\phi)}$ and case V$_>$ otherwise, where $R_1 = 16 \, o_\psi (l N_\psi)^2 4^{n_0}$ and $c_2(\phi)$ is an integer attached to $\phi$.

**Definition 2.1.5 (The counts).** Let P be one of the cases II, III, V$_\leq$, V$_>$ or Z. The *count for* P says: for each primitive $\psi$ there is $C$ such that for each host $h$ with character $\psi$, each $t$ for which $h$ is large, each odd prime $l$, each $0 < k < t$ and each $\phi \in X_h(k)$ in case P, the length $v_l(\phi, k)$ is finite and

$$\nu_l(\phi, k) \log l \leq (l N_h k)^C .$$

The *count for* I says: for each $\psi$ there are $C$ and two primes $r_1, r_2$ such that for each host $h$ with character $\psi$ and $r_1, r_2 < q, d$, each $t$ for which $h$ is large, and each finite set $S$ of odd primes, the lengths in case I are finite and $\sum_{l \in S} \log l \sum \nu_l(\phi, k) \leq (N_h t)^C$, where the inner sum is over the $(k, \phi)$ with $0 < k < t$, $\phi \in X_h(k)$ and $(l, k, \phi)$ in case I. The *count for* IV says: for $l \in B_\psi$ and $j \geq 0$ there is $C$ such that if $h$ is large for $t \geq 2$, $B \geq 0$, and the layer bound below holds, then for each $\phi$ of $h$ with $\phi_l$ of odd order, $\sum_{k=1}^{t-1} \nu_l(\phi, k) \leq B + (N_h t)^C$.

**Definition 2.1.6 (Layer bound).** Let $\psi$ be primitive, $l$ a prime and $j \geq 0$. Let $L_\psi(l) = \mathbb{Q}(\zeta_{l N_\psi})$. The *layer bound* $\Lambda(\psi, l, j, t, B)$ says: for each field $L_0$ isomorphic to $L_\psi(l)$ and each extension $L_1/L_0$ inside $L_0(\zeta_{l^\infty})$ of degree $l^j$, the field $L_1$ has $l$-bound $B$ below $t$.

Lean: `UpperTheory.V.HV.CountII` (also `CountI`, `CountIII`, `CountIV`, `CountV`, `CountVs`, `CountZ`, `UpperTheory.V.HV.LayerLe`).

**Lemma 2.1.7 (Reduction to characters).** Let $h$ be a host, $E$ a field of $h$, $l$ an odd prime, $k \geq 1$, and $\mathcal{O}$ as above with ramification index $e_\mathcal{O}$. Then

$$e_\mathcal{O} \, \ell^+_l(E, k) \leq \sum_{\phi \in X_h(k)} \big( v_l(\phi, k) + \lambda_l(N_h, k) \, e_\mathcal{O} \big),$$

where $\lambda_l(N_h, k) \leq (N_h k)^6$ is a loss term.

Lean: `UpperTheory.V.HV.redAll` (also `UpperTheory.V.HV.lossLe`).

*Proof.* We give the plan. The Galois group $G$ of $E$ over $\mathbb{Q}$ is $(\mathbb{Z}/N_h)^\times / H_h$, and its characters with values in $\mathcal{O}$ are the characters of $h$. Complex conjugation is the class of $-1$, so on the part of $\text{Ш}_l(E, k) \otimes \mathcal{O}$ where $G$ acts by $\phi$, it acts by $\phi(-1)$. The plus part therefore comes from the $\phi$ with $\phi(-1) = (-1)^k$, that is $\phi \in X_h(k)$. When $l$ does not divide $|G|$, the idempotents of $\mathcal{O}[G]$ split the module into these parts. The loss term bounds the defect of this splitting when $l$ divides $|G|$, and the defect of the comparison of each part with the module of $v_l(\phi, k)$. $\square$

**Lemma 2.1.8 (Bad primes).** Assume the counts for II, IV, V$_\leq$ and V$_>$. Let $\psi$ be primitive and $l \in B_\psi$. For each $j$ there is $C$ such that if $h$ is a host with character $\psi$, large for $t \geq 2$, $B \geq 0$ and $\Lambda(\psi, l, j, t, B)$ holds, then each field $E$ of $h$ has $\sum_{k=1}^{t-1} \ell^+_l(E, k) \log l \leq (N_h t)^C + C B$, with finite terms.

Lean: `UpperTheory.V.HV.sumIn`.

*Proof.* Put $M = N_h t$. Since $l \in B_\psi$, each triple $(l, k, \phi)$ with $\phi \in X_h(k)$ is in case II, IV or V. In cases II and V the counts give $\nu_l(\phi, k) \log l \leq (l N_h k)^{C'} \leq M^{2C'}$, since $l < q \leq N_h$ and $k < t$. In case IV the count bounds the whole sum over $k$ by $B + M^{C_4}$. There are at most $N_\psi$ characters $\phi$ of $h$ with $\phi_l$ of odd order. The reduction lemma sums over at most $N_h$ characters for each $k$. So

$$\log l \sum_{k=1}^{t-1} \ell^+_l \leq \log l \cdot N_\psi \, (B + M^{C_4}) + t N_h M^{2C'} + \log l \cdot N_h \, t M^6 .$$

Each term is at most a power of $M$ or a constant times $B$, since $\log l \leq l \leq M$ and $M \geq 3$. With $C = C_4 + 2C' + 9 + l N_\psi$ the sum is at most $M^C + C B$. $\square$

**Lemma 2.1.9 (Good primes).** Assume the counts for I, Z, II and III. For each primitive $\psi$ there are $C$ and primes $r_1, r_2$ such that if $h$ is a host with character $\psi$, $r_1, r_2 < q, d$, and $h$ is large for $t \geq 2$, then each field $E$ of $h$ has $\sum_{l \in S} \log l \sum_{k=1}^{t-1} \ell^+_l(E, k) \leq (N_h t)^C$ for each finite set $S$ of odd primes not in $B_\psi$.

Lean: `UpperTheory.V.HV.sumOut`.

*Proof.* Let $l \notin B_\psi$ be odd. A triple $(l, k, \phi)$ is in case I if $l - 1 \nmid 2k$. If $l - 1 \mid 2k$, then $l \leq 2k + 1 < 2t + 1 < q$, and the triple is in case Z, II or III: $\phi$ is trivial, or $\phi$ is nontrivial of odd order, or the eigenvalue condition of case II holds. The counts for Z, II and III bound each term by $M^{3C'}$ with $M = N_h t$, and only primes $l < 2t + 1$ occur, at most $M$ of them. The count for I bounds the sum over case I. The reduction lemma adds the loss terms. The constants $C_1 + 3 \max(C_Z, C_2, C_3) + 4$ and the primes $r_1, r_2$ of the count for I work. $\square$

**Theorem 2.1.10 (Plus bound at a point).** Assume the counts for I, II, III, V$_\leq$ and Z, Poitou-Tate duality, the finiteness of local cohomology, local Tate duality, and Lemma K with some constant. Let $\psi$ be primitive and $j : \mathbb{N} \to \mathbb{N}$. Then there are $C$ and primes $r_1, r_2$ such that: for each host $h$ with character $\psi$ and $r_1, r_2 < q, d$, each $t \geq 2$ for which $h$ is large, and each $B \geq 0$ with $\Lambda(\psi, l, j(l), t, B)$ for all $l \in B_\psi$, each field $E$ of $h$ has plus bound $(N_h t)^C + C B$ below $t$.

Lean: `UpperTheory.V.HV.pointHV_of_counts` (also `UpperTheory.V.HV.point`).

Lemma K is the bound on $H^2$ of Step 5 of [the proof chapter](/proof/vwin/). With the three duality statements it proves the count for V$_>$. The count for IV is proved outright, so it is not an assumption.

*Proof.* The count for V$_>$ comes from the four inputs above, and the count for IV holds. So the two lemmas apply. Let $S$ be a finite set of odd primes. Split $S$ into $S \cap B_\psi$ and $S \setminus B_\psi$. For $l \in B_\psi$ let $C_l$ be the constant of the lemma on bad primes for $j(l)$, and let $D = \sum_{l \in B_\psi} C_l$. Let $C_0, r_1, r_2$ come from the lemma on good primes, and put $b = |B_\psi|$ and $x = N_h t \geq 2$. Then the sum over $S$ is at most

$$b \, (x^D + D B) + x^{C_0} \leq x^{C} + C B, \qquad C = C_0 + D + b + bD .$$

The inequality uses $b + 1 \leq 2^b \leq x^b$. The finiteness of the terms comes from the two lemmas. $\square$

**Remark 2.1.11 (Formalization).** The plus and minus parts are `ShaPlus` and `ShaMinus`, with lengths `plusLen` and `minusLen`, and the bounds are `VVplusLe`, `VVminusLe` and `VVat` in [LengthEqAddEigen.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LengthEqAddEigen.lean#L107). The host and the cases are in [DirichletPrimeToLPartMulLPowerPart.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/DirichletPrimeToLPartMulLPowerPart.lean), the bad primes in [StmtFields.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/StmtFields.lean#L75). We did not unfold the length $v_l(\phi, k)$ (`Chr.V'`), its size $\nu_l$ (`Chr.nrm`), the eigenvalue condition of case II (`EV`), the integer $c_2(\phi)$ or $n_0$, and we did not open the proofs of the reduction lemma and the loss bound; the proof given for the reduction lemma is the plan, not the code. The constant $e_\mathcal{O}$ is `eO`. The count for V$_>$ is `countVs`, from `PoitouTateDuality`, `LocalFinitenessK`, `LocalTateDualityK` and `LemmaK`, and the count for IV is `countIV`, proved with $C = N_{L_\psi(l)}^j + 3$. Theorem (plus bound at a point) is `PointHV`; its proof is `point (sumIn …) (sumOut …)`, and `sumOut` runs under `maxHeartbeats 400000`.
