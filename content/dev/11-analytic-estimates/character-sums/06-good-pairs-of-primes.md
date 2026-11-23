---
title: Good pairs of primes
decls:
  - QH.pair_share
  - QH.pair_exists
  - QH.pairEx
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Good pairs of primes

This section finds, at each large height $Y$, a pair of primes $q < d$ with prescribed congruences and sizes such that all twists of the characters of a fixed modulus by $(\cdot/q)$ and $(\cdot/d)$ lie in boxes. A character lies in a box when it has a zero-free box and a small smoothed prime sum. The proof applies [the stage theorem](/entry/stage/) twice: first to the primes $q$, then, for a good $q$, to the primes $d$. The final form is used in the supply of admissible data ([Theorem 3.3.5 of Volume 15](/entry/supply-of-adm-of/)).

We keep the notation of the previous section: $\mathcal{P}(m_0, a_0, U)$, the boxes, and $(n/q)$ for the [[Jacobi symbol|0ADTQBXRMC]]. Throughout, $Y$ is large, $0 < \varepsilon < 1/52$, and
$$w = Y^{\varepsilon/5}.$$

**Definition 6.6.1 (Primes of the first and second kind).** For $z > 0$ the primes of the first kind are $\mathcal{P}_1(z) = \mathcal{P}(8, 3, e^z)$: the primes $q \equiv 3 \pmod 8$ with $e^{z/2} < q \leq e^z$. For a prime $q$ let $m(z, q) = q\prod_{3 \leq p \leq z}p$, the product over primes. For $z' > 0$ the primes of the second kind are the primes $d$ with
$$d \equiv 7 \pmod{16}, \qquad m(z, q) \mid d + 1, \qquad e^{z'/2} < d \leq e^{z'}.$$
Their set is $\mathcal{P}_2(z, z', q)$.

Lean: `QH.primePairSetFirst` (also `QH.primeSetTwoBounds`, `Formalism.HermitianLattices.ZeroFreeRegionGL2.oddM`).

**Definition 6.6.2 (Good primes).** Let $N_0 \geq 1$ and let $C, \tau, Y, X, z, z'$ be real. A prime $q$ is *good* if for every [[Dirichlet character|JR4QSEFXWF]] $\xi$ modulo $N_0$ the pair $(n \mapsto \xi(n)(n/q), N_0q)$ lies in the box $(N_0e^z, C, \tau, Y, X)$. A prime $d$ is *good for $q$* if for every $\xi$ modulo $N_0$ and every $a \in \{0, 1\}$ the pair $(n \mapsto \xi(n)(n/q)^a(n/d), N_0qd)$ lies in the box $(N_0e^{z + z'}, C, \tau, Y, X)$.

Lean: `QH.GoodQ` (also `QH.GoodD`).

**Lemma 6.6.3 (Most primes of the first kind are good).** There is $C > 0$ such that for all $0 < \varepsilon < 1/52$, $\tau > 0$, $K \geq 1$, $\eta > 0$ and $N_0 \geq 1$ there is $Y_0$ with the following property. For $Y \geq Y_0$ the set $\mathcal{P}_1(w)$ is not empty, and every subset of $\mathcal{P}_1(w)$ that consists of primes that are not good for $(N_0, C, \tau, Y, Y^K, w)$ has at most $\eta|\mathcal{P}_1(w)|$ elements.

Lean: `QH.stage1`.

*Proof.* Apply the stage theorem with $m_0 = 8$, $a_0 = 3$, $U = e^w$ and $F = N_0$. For $\Xi$ take, for each $\xi$ modulo $N_0$, the primitive character that induces $\xi$; its modulus is at most $N_0$, and $|\Xi|$ is at most the number of characters modulo $N_0$. The parameters are admitted: $\log U = w$, and $\tfrac14\log^2Y\log 8 \leq 2\log^2Y \leq w$ for large $Y$. The only prime factor $2$ of $8$ is at most $w$. Also $N_0 \leq e^{w/2} = U^{1/2}$ for large $Y$. If $q$ is not good, there are $\xi$ and a primitive $\psi$ that agrees with $\xi\cdot(\cdot/q)$ on the integers prime to $N_0q$ and does not lie in the box of height $N_0e^w = FU$. The primitive character $\xi'$ that induces $\xi$ agrees with $\xi$ on these integers. So $q$ is bad for the stage theorem with $\xi' \in \Xi$ and $M = N_0q$. $\square$

**Lemma 6.6.4 (Most primes of the second kind are good).** There is $C > 0$ such that for all $0 < \varepsilon < 1/52$, $\tau > 0$, $K \geq 1$, $\eta > 0$ and $N_0 \geq 1$ there is $Y_0$ with the following property. Let $Y \geq Y_0$, let $w\log^2Y \leq z' \leq K^2w\log^2Y$, and let $q \in \mathcal{P}_1(w)$. Then $\mathcal{P}_2(w, z', q)$ is not empty, and every subset of it that consists of primes $d$ that are not good for $q$, for $(N_0, C, \tau, Y, Y^K, w, z')$, has at most $\eta|\mathcal{P}_2(w, z', q)|$ elements.

Lean: `QH.stage2`.

*Proof.* Apply the stage theorem with $\varepsilon' = 6\varepsilon/5 \leq 1/4$, $U = e^{z'}$, $m_0 = 16\,m(w, q)$ and $F = N_0e^w$.

1. *The progression.* For large $Y$ we have $q > e^{w/2} > w$, so $m(w, q)$ is odd and squarefree. By the Chinese remainder theorem the conditions $d \equiv 7 \pmod{16}$ and $d \equiv -1 \pmod{m(w, q)}$ form one class $a_0$ modulo $m_0$, prime to $m_0$. So $\mathcal{P}_2(w, z', q) = \mathcal{P}(m_0, a_0, U)$.
2. *Admitted.* We have $\log m_0 \leq 4w$, so $\tfrac14\log^2Y\log m_0 \leq w\log^2Y \leq z'$. Next $Y^{\varepsilon'/6} = w \leq z'$. Finally $z' \leq K^2w\log^2Y \leq Y^{\varepsilon/25}w\log^2Y = Y^{\varepsilon'/5}\log^2Y$ for large $Y$.
3. *Primes of $m_0$.* The prime $2$ and the primes $p \leq w$ are at most $Y^{\varepsilon'/5}$. The prime $q$ exceeds $e^{w/2} > Y^{400K}$ for large $Y$.
4. *The characters.* $F \geq 1$, and $F \leq e^{z'/2}$ since $\log N_0 + w \leq z'/2$. For each $\xi$ modulo $N_0$ and $a \in \{0, 1\}$, $\Xi$ holds a primitive character that agrees with $\xi\cdot(\cdot/q)^a$ on the integers prime to $N_0q$. Its modulus is at most $N_0q \leq F$. Hence $|\Xi|$ is at most twice the number of characters modulo $N_0$.

A prime $d$ that is not good for $q$ gives $\xi$ and $a$ such that the pair $(\xi\cdot(\cdot/q)^a\cdot(\cdot/d), N_0qd)$ does not lie in the box of height $N_0e^{w + z'} = FU$. The element of $\Xi$ for $(\xi, a)$ agrees with $\xi\cdot(\cdot/q)^a$ on the integers prime to $N_0qd$. So $d$ is bad for the stage theorem with $M = N_0qd$. $\square$

**Theorem 6.6.5 (Share of good pairs).** There is $C > 0$ such that for all $0 < \varepsilon < 1/52$, $\tau > 0$, $K \geq 1$, $\eta > 0$ and $N_0 \geq 1$ there is $Y_0$ with the following property. Let $Y \geq Y_0$, $X \leq Y^K$ and $w\log^2Y \leq z' \leq K^2w\log^2Y$. Then $\mathcal{P}_1(w)$ is not empty, and there is $G_1 \subseteq \mathcal{P}_1(w)$ with $|G_1| \geq (1 - \eta)|\mathcal{P}_1(w)|$ such that each $q \in G_1$ is good for $(N_0, C, \tau, Y, X, w)$. Each $q \in G_1$ also has the following property: $\mathcal{P}_2(w, z', q)$ is not empty, and there is $G_2 \subseteq \mathcal{P}_2(w, z', q)$ with $|G_2| \geq (1 - \eta)|\mathcal{P}_2(w, z', q)|$ such that each $d \in G_2$ is good for $q$, for $(N_0, C, \tau, Y, X, w, z')$.

Lean: `QH.pair_share`.

*Proof.* Let $C_1$ and $C_2$ be the constants of the two lemmas and put $C = \max(C_1, C_2)$. Take for $G_1$ the set of good primes in $\mathcal{P}_1(w)$ for the constant $C_1$ and the range $[Y, Y^K]$. Its complement in $\mathcal{P}_1(w)$ has at most $\eta|\mathcal{P}_1(w)|$ elements by the first lemma, so $|G_1| \geq (1 - \eta)|\mathcal{P}_1(w)|$. The second lemma gives $G_2$ in the same way. Lying in a box is monotone: it stays true when $C$ grows, since $\log Y \geq 0$, and when the range $[Y, X]$ shrinks. So the good primes for $C_1$ or $C_2$ and $Y^K$ are good for $C$ and $X$. $\square$

**Definition 6.6.6 (Rows).** Let $z, z' > 0$. Two numbers $q, d$ satisfy the *row conditions* if $q$ is a prime with $q \equiv 3 \pmod 8$ and $z/2 < \log q \leq z$; $d$ is a prime with $d \equiv 7 \pmod{16}$ and $z'/2 < \log d \leq z'$; $q < d$; and every odd prime $p$ with $p \leq z$ or $p = q$ divides $d + 1$.

Lean: `QH.Rows`.

**Theorem 6.6.7 (A good pair exists).** There is $C > 0$ such that for all $0 < \varepsilon < 1/52$, $\tau > 0$, $K \geq 1$ and $N_0 \geq 1$ there is $Y_0$ with the following property. Let $Y \geq Y_0$, $X \leq Y^K$ and $w\log^2Y \leq z' \leq K^2w\log^2Y$. Then there are $q, d$ that satisfy the row conditions for $(w, z')$, with $q > N_0$, such that $q$ is good for $(N_0, C, \tau, Y, X, w)$ and $d$ is good for $q$, for $(N_0, C, \tau, Y, X, w, z')$.

Lean: `QH.pair_exists`.

*Proof.* Apply the share theorem with $\eta = 1/2$. Then $G_1$ is not empty; take $q \in G_1$. Then $G_2$ is not empty; take $d \in G_2$. The row conditions follow from the definitions of $\mathcal{P}_1$ and $\mathcal{P}_2$, except $q < d$. For $Y \geq e^2$ we have $\log^2Y \geq 4$, so $z' \geq 2w$ and $\log q \leq w \leq z'/2 < \log d$. Finally, for large $Y$ we have $w \geq 2N_0$, so $q > e^{w/2} \geq e^{N_0} > N_0$. $\square$

The last theorem restates this result in the form used later. Recall the [weighted prime sum](/entry/thin/) $g_\chi$ of a character $\chi \neq \chi_0$; it equals $G_\chi$ of the previous section.

**Definition 6.6.8 (Window pair, good pair).** Let $0 < \varepsilon$, let $Y \geq 1$, and put $w = Y^{\varepsilon/5}$ and $w' = w\log^2Y$. A *window pair* is a pair of primes $(q, d)$ with $q \equiv 3 \pmod 8$, $w/2 < \log q \leq w$, $d \equiv 7 \pmod{16}$, $w'/2 < \log d \leq w'$, $q \mid d + 1$, and $p \mid d + 1$ for each odd prime $p \leq w$. For a function $\xi$ on $\mathbb{N}$ and $i, j \in \{0, 1\}$ let
$$\mathrm{tw}_{ij}(\xi)(n) = \xi(n)\Bigl(\frac nq\Bigr)^i\Bigl(\frac nd\Bigr)^j.$$
Let $M \geq 1$ and $X \geq Y$. The pair $(q, d)$ is *good* for $(M, \varepsilon, Y, X)$ if:

1. $(q, d)$ is a window pair and $\gcd(M, qd) = 1$;
2. for every character $\xi$ modulo $M$, every $(i, j) \neq (0, 0)$, every primitive character $\chi$ that agrees with $\mathrm{tw}_{ij}(\xi)$ on the integers prime to $2Mqd$, and every $y \in [Y, X]$,
$$|g_\chi(y)| \leq y^{1/2 + \varepsilon/2}, \qquad \Bigl|\frac{L'}{L}(1, \chi)\Bigr| \leq 4\log y;$$
3. for every real primitive character $\rho$ whose modulus divides $8M$, every $(i, j) \neq (0, 0)$ and every primitive $\chi$ that agrees with $\mathrm{tw}_{ij}(\rho)$ on the integers prime to $2Mqd$, $L(s, \chi) \neq 0$ for $\mathrm{Re}\,s > 1 - 1/400$ and $|\mathrm{Im}\,s| \leq 8Me^{w + jw'}$.

Lean: `UpperTheory.Top.PairGood` (also `UpperTheory.Top.WinPair`, `UpperTheory.Top.tw`, `UpperTheory.Top.height`, `UpperTheory.Top.ZeroBox`).

**Theorem 6.6.9 (Good pairs exist).** For every $M \geq 1$, every $0 < \varepsilon < 1/52$ and every $A \geq 1$ there is $Y_1$ such that for every $Y \geq Y_1$ there are $q, d$ such that $(q, d)$ is good for $(M, \varepsilon, Y, Y^A)$.

Lean: `QH.pairEx` (also `UpperTheory.Top.PairEx`).

*Proof.* Apply the existence theorem with $\tau = \varepsilon/2$, $K = A$, $N_0 = 8M$, $X = Y^A$ and $z' = w\log^2Y$. It gives $(q, d)$ with the row conditions, $q > 8M$, $q$ good and $d$ good for $q$.

1. *Window pair.* The row conditions give it. Since $d > q > 8M$, neither prime divides $M$, so $\gcd(M, qd) = 1$.
2. *Boxes.* Let $\xi$ be a character modulo $M$ and lift it to the modulus $8M$; the lift agrees with $\xi$ on the integers prime to $8M$. Let $\chi$ be primitive and agree with $\mathrm{tw}_{ij}(\xi)$ on the integers prime to $2Mqd$. If $j = 1$, then $\chi$ also agrees with it on the integers prime to $8Mqd$, and $d$ good for $q$ puts $\chi$ in the box of height $8Me^{w + w'}$. If $j = 0$, then $i = 1$. A primitive character is determined by its values on the integers prime to any fixed $M' \neq 0$. So $\chi$ is the primitive character that induces the character $\xi\cdot(\cdot/q)$ modulo $8Mq$, and $\chi$ agrees with $\xi\cdot(\cdot/q)$ on the integers prime to $8Mq$. So $q$ good puts $\chi$ in the box of height $8Me^w$. The same holds with a real $\rho$ in place of $\xi$. This gives clause 3, and the bound on $g_\chi = G_\chi$ in clause 2, since $\chi \neq 1$.
3. *The logarithmic derivative.* The height $Q$ of the box satisfies $Y^{\varepsilon/6} \leq \log Q \leq 3w\log^2Y$ when $Y \geq e^{1 + \log 8M}$. For $Q$-good $\chi$ and such $Q$, a contour bound gives $|L'/L(1, \chi)| \leq 1000\log\log Q + O(1)$. Since $\log\log Q \leq (\varepsilon/5 + o(1))\log Y$ and $200\varepsilon < 4$, this is at most $4\log Y \leq 4\log y$ for large $Y$. $\square$

The condition $\varepsilon < 1/52$ enters only in step 3: it makes $200\varepsilon$ less than $4$ with room to spare.

**Remark 6.6.10 (Formalization).** The definitions of the prime sets and of good primes are in [PrimeSetTwoBounds.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PrimeSetTwoBounds.lean#L45). The two lemmas are `QH.stage1` in [Stage1Succ.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/Stage1Succ.lean#L36) and `QH.stage2` in [CharOf.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/CharOf.lean#L61). The share theorem is in [PairShare.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PairShare.lean#L26), the existence theorem in [PairExists.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PairExists.lean#L9), and the last theorem in [pairEx.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/pairEx.lean#L112). The good pair is defined in [PairGood.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/PairGood.lean#L18) and the window pair in [ExistsPageN.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean#L27). The proofs above follow the code. Step 1 of the second lemma is the lemma `exists_coprime_primePairSetSecond_eq_PPset`, and the change of modulus in step 2 of the last proof is `ind_drop`; we have not opened their proofs. The contour bound in step 3 is `QH.kappa4`. The box of the existence theorem also gives $|L'/L(1, \chi)| \leq C\log Y$; the proof of the last theorem does not use this bound and calls `QH.kappa4` for the constant $4$. Clause 2 holds for every $\xi$ modulo $M$, but clause 3 is stated only for real $\rho$ of modulus dividing $8M$, although the proof gives it for all $\xi$. The weighted prime sum in the definition is `Formalism.HC.An.gChi`, which agrees with $G_\chi$ for $\chi \neq 1$ by the private lemma `pairEx_g`.
