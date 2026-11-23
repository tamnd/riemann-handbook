---
title: Semisimplicity at a newform
decls:
  - GlobalTheory.HeckeFamilyMatrices.ul_semisimple
  - GlobalTheory.HeckeFamilyMatrices.hecke_semisimple_at_newform
  - GlobalTheory.T.hecke_semisimple_generalised_eigen_newform_gamma1Gamma0
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Semisimplicity at a newform

Let $g$ be a newform of odd weight $k \geq 3$, let $l$ be a prime not dividing the level, and let $\alpha$ be a root of the Hecke polynomial of $g$ at $l$. The Hecke projector of the later sections cuts out the part of a cohomology group where $T_q$ acts by $a_q(g)$, $U_l$ by $\alpha$ and the diamond operators by the character of $g$. To build the projector from polynomials in the Hecke operators we need the generalised eigenspace for this eigensystem to be an eigenspace. This section proves that, first for $U_l$ on cusp forms and then for all operators at once on the cocycles of $\Gamma_1(N) \cap \Gamma_0(l)$. The result is used in [the semisimple potentials theorem](/entry/ss-pot-b-at-newform/).

We keep the notation of the [Eichler and Shimura decomposition](/entry/exists-per-add-cj-per/): $V_w$, $Z^1$, $B^1$, the period cocycle $r_f$, and the Hecke families $T_q$, $U_l$, $\langle d \rangle$. Put $\Gamma = \Gamma_1(N) \cap \Gamma_0(l)$.

**Definition 6.4.1 (Newform).** Let $k \geq 1$. A *newform of weight $k$* is a level $M \geq 1$, a Dirichlet character $\chi$ modulo $M$ and a cusp form $g = \sum_{n \geq 1} a_n q^n \in S_k(\Gamma_1(M))$ such that: $g|_k \gamma = \chi(d_\gamma) g$ for $\gamma \in \Gamma_0(M)$; $a_1 = 1$; $T_p g = a_p g$ for every prime $p \nmid M$; and for every proper divisor $M'$ of $M$, every character $\chi'$ modulo $M'$ and every $h \in S_k(\Gamma_1(M'))$ with character $\chi'$, if $T_p h = a_p h$ for all but finitely many primes $p$, then $h = 0$. Its *Hecke polynomial* at $p$ is $X^2 - a_p X + \chi(p) p^{k-1}$.

This is the [newform of Atkin, Lehner and Li](/learn/automorphic-forms/#modular-forms), with the multiplicity one property built into the last condition.

**Lemma 6.4.2 ($U_l$ is semisimple at $\alpha$).** Let $N \geq 5$, let $l$ be a prime with $l \nmid N$, let $k \geq 3$, let $\chi$ be a Dirichlet character modulo $N$, and let $\alpha \in \mathbb{C}$ with
$$
\alpha^2 \neq \chi(l)\, l^{k-1}, \qquad \alpha^2 \neq \chi(l)\, l^{k-2}.
$$
Let $f \in S_k(\Gamma)$ satisfy $f|_k \gamma = \chi(d_\gamma) f$ for all $\gamma \in \Gamma_0(Nl)$, and let $(U_l - \alpha)^n f = 0$ for some $n \geq 0$. Then $U_l f = \alpha f$.

Lean: `GlobalTheory.HeckeFamilyMatrices.ul_semisimple`.

*Proof.* Let $O$ be the $l$-old space: the functions $f_1 + f_2|_k \begin{pmatrix} l & 0 \\ 0 & 1 \end{pmatrix}$ with $f_1, f_2 \in S_k(\Gamma_1(N))$ of character $\chi$ on $\Gamma_0(N)$. Two facts are used. First, for $f$ as in the lemma, $U_l^2 f - \chi(l) l^{k-2} f \in O$. This is the classical fact that $U_l^2 = \chi(l) l^{k-2}$ on the $l$-new part. Second, $U_l$ maps $O$ into $O$, and on $O$ every vector killed by a power of $U_l - \alpha$ is killed by $U_l - \alpha$. On a pair $(f_1, f_2)$ with $f_1$ an eigenform of $T_l$ with eigenvalue $a$, the operator $U_l$ acts on the span of $f_1$ and $f_1|_k \mathrm{diag}(l, 1)$ with characteristic polynomial $X^2 - a X + \chi(l) l^{k-1}$, and its roots are distinct at $\alpha$ because $\alpha^2 \neq \chi(l) l^{k-1}$.

Now put $c = \chi(l) l^{k-2}$. The polynomials $(X - \alpha)^n$ and $X^2 - c$ are coprime, since $\alpha^2 \neq c$. Choose $A, B$ with $A(X)(X - \alpha)^n + B(X)(X^2 - c) = 1$. Then
$$
f = A(U_l)(U_l - \alpha)^n f + B(U_l)(U_l^2 - c) f = B(U_l)(U_l^2 - c) f \in O,
$$
since $O$ is stable under $U_l$. So $f$ lies in $O$ and is killed by a power of $U_l - \alpha$, and by the second fact $U_l f = \alpha f$. $\square$

**Theorem 6.4.3 (Semisimplicity at a newform).** Let $k \geq 3$ be odd and let $g$ be a newform of weight $k$, level $M$ and character $\chi$. Let $N \geq 5$ with $M \mid N$, let $l$ be a prime with $l \nmid N$, and let $\alpha \in \mathbb{C}$ with
$$
\alpha^2 - a_l \alpha + \chi(l) l^{k-1} = 0, \qquad \alpha^2 \neq \chi(l) l^{k-1}, \qquad \alpha^2 \neq \chi(l) l^{k-2}.
$$
For each prime $q \nmid Nl$ let $\sigma_q \in \Gamma_0(Nl)$ have lower right entry $\equiv q \pmod N$, and for each $d \in (\mathbb{Z}/N)^\times$ let $\sigma_d \in \Gamma_0(Nl)$ have lower right entry $\equiv d \pmod N$. Let $w = k - 2$, let $z \in Z^1(\Gamma, V_w)$ and let $n \geq 0$. Assume that
$$
\begin{aligned}
(T_q - a_q)^n z &\in B^1 \quad \text{for all primes } q \nmid Nl, \\
(U_l - \alpha)^n z &\in B^1, \\
(\langle d \rangle - \chi(d))^n z &\in B^1 \quad \text{for all } d \in (\mathbb{Z}/N)^\times.
\end{aligned}
$$
Then the same holds with $n = 1$.

Lean: `GlobalTheory.HeckeFamilyMatrices.hecke_semisimple_at_newform` (also `GlobalTheory.T.hecke_semisimple_generalised_eigen_newform_gamma1Gamma0`, a second name).

*Proof.* By the [Eichler and Shimura decomposition](/entry/exists-per-add-cj-per/), $z \equiv r_f + \overline{r_h}$ modulo $B^1$ with $f \in M_k(\Gamma)$ and $h \in S_k(\Gamma)$. The families $T_q$, $U_l$ and $\langle d \rangle$ represent double cosets of $\Gamma$, so the Hecke operators on cocycles preserve $Z^1$ and $B^1$. The period map is compatible with them: $T r_f \equiv r_{Tf}$ modulo $B^1$ for each of the three operators, and $T \overline{r_h} = \overline{T r_h}$, since the matrices are integral. As the map $(f, h) \mapsto r_f + \overline{r_h}$ is injective modulo $B^1$, we get for every operator $T$ and every $a \in \mathbb{C}$:
$$
(T - a)^n z \in B^1 \iff (T - a)^n f = 0 \text{ and } (T - \bar a)^n h = 0.
$$

*$f$ is a cusp form.* Choose a prime $q \equiv 1 \pmod{Nl}$, by Dirichlet's theorem. Then $T_q f - (1 + q^{k-1}) f$ is a cusp form, since $T_q$ acts on Eisenstein series of this level by $1 + q^{k-1}$. By the Ramanujan bound for $g$ (Deligne), $|a_q| \leq 2 q^{(k-1)/2} < 1 + q^{k-1}$, so $a_q \neq 1 + q^{k-1}$. From $(T_q - a_q)^n f = 0$ and the coprimality of $(X - a_q)^n$ and $X - (1 + q^{k-1})$, the form $f$ is a cusp form.

*The operators $T_q$.* On $S_k(\Gamma)$ the operators $T_q$ with $q \nmid Nl$ are normal for the Petersson product, hence semisimple. So $(T_q - a_q)^n f = 0$ gives $T_q f = a_q f$, and $(T_q - \bar a_q)^n h = 0$ gives $T_q h = \bar a_q h$.

*The diamond operators.* Each $\langle d \rangle$ has finite order, so it is semisimple, and $\langle d \rangle f = \chi(d) f$, $\langle d \rangle h = \bar\chi(d) h$. So $f$ has character $\chi$ on $\Gamma_0(Nl)$ and $h$ has character $\bar\chi$.

*The operator $U_l$.* Apply the lemma to $f$ with $\chi$ and $\alpha$, and to $h$ with $\bar\chi$ and $\bar\alpha$. The conditions on $\bar\alpha$ follow from those on $\alpha$ by conjugation, since $\bar\chi(l) = \overline{\chi(l)}$. So $U_l f = \alpha f$ and $U_l h = \bar\alpha h$.

Going back through the equivalence gives the three statements with $n = 1$. $\square$

The Hecke polynomial condition on $\alpha$ is not used: the proof works for any $\alpha$ that satisfies the two inequalities. It explains which $\alpha$ the later sections use.

**Remark 6.4.4 (Formalization).** In the theorem the hypothesis that $\alpha$ is a root of the Hecke polynomial is introduced as an anonymous variable and never used ([HeckeSemisimpleGeneralisedEigenNewformGamma1Gamm.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/HeckeSemisimpleGeneralisedEigenNewformGamma1Gamm.lean#L336)). The statement with the second name is a wrapper under `maxHeartbeats 1000000`. The facts on the $l$-old space, the compatibility of the period map with Hecke operators, the cuspidality via a prime $q \equiv 1 \pmod{Nl}$ and the semisimplicity of $T_q$ on cusp forms were read as statements. The bound $a_q \neq 1 + q^{k-1}$ is a lemma of the development; the argument via Deligne's bound above is one way to see it.
