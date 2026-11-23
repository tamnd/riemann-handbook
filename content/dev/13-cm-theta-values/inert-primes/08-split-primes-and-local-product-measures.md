---
title: Local product measures and jets at split primes
decls:
  - Formalism.L2.Ker.md_prod
  - Formalism.L2.Ker.muProdLaw_of
  - Formalism.L2.Ker.Cd.CarC.thEquivP_ambOf_tiesD
  - Formalism.L2.Ker.Test.jetAtSplit_ambOf
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local product measures and jets at split primes

The kernels of the earlier sections are built from theta distributions, one for each step of a column, and each distribution carries a product of local measure factors. This section proves three facts about these objects. First, the product of the local factors at an element $x/\bar{x}$ is the infinity part of a Hecke character; this is a product formula. Second, from the product formula and Hilbert's Theorem 90, the local measure changes by a character of the determinant when a unitary map moves the lattice and the frames. Third, the theta distribution of a step is equivariant for the unitary groups; [the chain of theta distributions with a character](/entry/ch-th-ok-chi/) of Volume 14 uses this. A separate result of the section bounds the jets of the ambient datum at a split prime $p$; [the jet bound for the ambient datum](/entry/jet-split-amb-holds/) uses it.

### Measures and the product formula

Let $E$ be a CM field with totally real subfield $F$, let $x \mapsto \bar{x}$ be complex conjugation on $E$, let $K$ be a field of values with an embedding $\sigma_0 : K \to \mathbb{C}$, and let $\tau$ run through the CM type of $E$, with $\tau : E \to K$. We assume the conditions on $E$, $F$ and $K$ that make $E/F$ an abelian unramified setting, and that the prime data are valid. A *selection* is a map $v \mapsto \mathrm{sel}(v)$ from the finite places of $F$ to the primes of $E$ such that $\mathrm{sel}(v)$ lies over $v$. The prime data, the selection and a twist $\xi$ give a finite set $S_B$ of primes of $E$, the *row primes*. The prime data also contain two primes $g_0$ and $g_1$; we say that $\xi$ is *off $g$* if no place of $F$ below a prime of $E$ over $g_0$ or $g_1$ is a ramified place of $\xi$.

The *ties* for weights $W$, characters, the selection, $\xi$, local constants and a global character $G$ are four conditions. They include: for each level $i$ there is a Hecke character $\mu_{0,i}$ of $E$ in $G$, unramified outside the primes over $g_0 g_1$, with infinity type $n$ such that $n_\tau = -2e_{\tau,i}$, where $e_{\tau,i}$ is the weight of row $\tau$ at level $i$; and the row weights of each word are the weights of the rows.

At a level $i$, the data give a unit $m_U(P) \in K^\times$ for each prime $P$ of $E$, and a local factor $\mu_{i,P} : E \to K$ for each $P \in S_B$. For $y \in E^\times$ and a place $v$ of $F$, put $z_v(y) = 1$ if $v$ is below a prime of $S_B$, and $z_v(y) = m_U(\mathrm{sel}(v))^{\mathrm{ord}_{\mathrm{sel}(v)}(y)}$ otherwise. Only finitely many $z_v(y)$ are not $1$.

**Theorem 6.8.1 (Product formula for the local factors).** Assume the conditions on $E$, $F$ and $K$, valid prime data, a selection, a twist that is off $g$, and the ties. Let $i < m$ and $x \in E^\times$. Then
$$\sigma_0\Bigl(\prod_v z_v(x/\bar{x})\cdot\prod_{P \in S_B}\mu_{i,P}(x/\bar{x})\Bigr) = \mu_{0,i,\infty}(x),$$
where $\mu_{0,i,\infty}$ is the infinity part of $\mu_{0,i}$.

Lean: `Formalism.L2.Ker.md_prod`

*Proof.* For a place $v$ of $F$, let $\lambda_H(v)$ be the $v$-component of $\mu_{0,i}$ on $E^\times$, and let $\lambda_\xi(v)$ be the $v$-component of $\xi$. The Hecke character is unramified outside the primes over $g_0 g_1$, so by the product formula for Hecke characters $\prod_v \lambda_H(v)(x) = \mu_{0,i,\infty}(x)^{-1}$, with finitely many factors not $1$. The twist satisfies $\prod_v \lambda_\xi(v)(x) = 1$. Put $f(v) = \bigl(\lambda_H(v)(x)\,\sigma_0(\lambda_\xi(v)(x))\bigr)^{-1}$. Then $\prod_v f(v) = \mu_{0,i,\infty}(x)$.

Let $R$ be the set of places of $F$ below a prime of $S_B$. Split the product of $f$ into the product over $v \notin R$ and the product over $v \in R$. For $v \notin R$, the ties give $\sigma_0(z_v(x/\bar{x})) = f(v)$. For $v \in R$, $z_v = 1$. For $P \in S_B$ over $v$, the ties and the fact that $\xi$ is off $g$ give $\sigma_0(\mu_{i,P}(x/\bar{x})) = f(v)$. Since $\xi$ is off $g$, two distinct primes of $S_B$ lie over distinct places of $F$, so $P \mapsto v$ is a bijection from $S_B$ onto $R$. Thus the left side is $\prod_{v \notin R} f(v)\cdot\prod_{v \in R} f(v) = \mu_{0,i,\infty}(x)$. $\square$

### The product law

For a self-dual lattice $N$ in $E^n$ and a prime $P$ of $E$, fix a *frame* of $N$ at $P$: an automorphism of $E^n$ that carries the standard lattice at $P$ onto the localization of $N$ at $P$. A *frame family* is a choice of an automorphism $\mathrm{fr}_P$ of $E^n$ for each $P \in S_B$. The *local measure* at level $i$ is
$$\mu_i(N, \mathrm{fr}) = \prod_v c_v(N)\cdot\prod_{P \in S_B}\mu_{i,P}(\det \mathrm{fr}_P),$$
where $c_v(N) = 1$ if $v$ is below a prime of $S_B$, and $c_v(N) = m_U(\mathrm{sel}(v))^{\mathrm{ord}_{\mathrm{sel}(v)}\det(\text{frame of } N)}$ otherwise. Let $U(n)$ be the group of $E$-linear automorphisms of $E^n$ that keep the standard hermitian form.

**Definition 6.8.2 (Product law).** The local measure satisfies the *product law* of rank $n$ and exponent $e : \tau \mapsto e_\tau \in \mathbb{Z}$ if for every $\gamma \in U(n)$, every self-dual lattice $N$ in $E^n$ and every frame family,
$$\mu_i(\gamma N, \gamma\,\mathrm{fr}) = \Bigl(\prod_\tau \tau(\det\gamma)^{-e_\tau}\Bigr)\,\mu_i(N, \mathrm{fr}).$$

**Theorem 6.8.3 (Product law of the local measures).** Assume the hypotheses of the product formula, let $i < m$, and let $e_\tau \in \mathbb{Z}$ equal the weight of row $\tau$ at level $i$ for every $\tau$. Then for every $n$, the local measure at level $i$ satisfies the product law of rank $n$ and exponent $e$.

Lean: `Formalism.L2.Ker.muProdLaw_of`

*Proof.* Let $\gamma \in U(n)$ and put $z = \det\gamma$. Since $\gamma$ keeps the hermitian form, $z\bar{z} = 1$. By Hilbert's Theorem 90 for the quadratic extension $E/F$, there is $x \in E^\times$ with $z = x/\bar{x}$. For a prime $Q$ of $E$, $\mathrm{ord}_Q\det$ of the frame of $\gamma N$ is $\mathrm{ord}_Q z$ plus $\mathrm{ord}_Q\det$ of the frame of $N$. Each $\mu_{i,P}$ is multiplicative on $E^\times$. Hence
$$\mu_i(\gamma N, \gamma\,\mathrm{fr}) = \Bigl(\prod_v z_v(z)\cdot\prod_{P \in S_B}\mu_{i,P}(z)\Bigr)\,\mu_i(N, \mathrm{fr}).$$
Since $\sigma_0$ is injective, it is enough to compute $\sigma_0$ of the factor in parentheses. By [the product formula](/entry/md-prod/), it is $\mu_{0,i,\infty}(x)$. The ties give the infinity type $n_\tau = 2(-e_\tau)$. For a Hecke character with this infinity type, $\mu_{0,i,\infty}(x) = \prod_\tau \sigma_0\bigl(\tau(x/\bar{x})\bigr)^{-e_\tau}$. This is $\sigma_0\bigl(\prod_\tau \tau(z)^{-e_\tau}\bigr)$. $\square$

### Equivariance of a step

Let the curve data be of the second kind, with a seam $s$, a curve ideal $\mathfrak{c}$, a twelfth root $\delta$ for it, a base $B$, the character $\chi$ and constants $c_D$. These give an ambient datum $A$. For a word $u$ and a level $i < m$, the data give the step distribution $\Theta_i$: it sends two self-dual lattices $N$ and $N'$ of ranks $N_i$ and $N_{i+1}$, two frame families, a number $c$ and a map $x : E^{N_i} \to E^{N_{i+1}}$ to a linear map between the column spaces $V_i$ and $V_{i+1}$. The unitary groups act on the column spaces by representations $\rho_i$ and $\rho_{i+1}$. Put $D = c_A c_B(u)$, the product of the two moduli of the word.

**Theorem 6.8.4 (Equivariance of the theta step).** Assume that $s$ is valid, that $\mathfrak{c}$ is a curve ideal with twelfth root $\delta$, that $\chi$ is the character of the data, the hypotheses of the product formula, and that the word $u$ has a positive count. Let $i < m$, let $e_\tau \in \mathbb{Z}$ equal the weight of row $\tau$ at level $i$, assume the lattice hypotheses for $A$ at ranks $N_i$ and $N_{i+1}$ on the set of primes of $u$, and assume that the jets of $A$ are rational of the step degree. Then for $\gamma \in U(N_i)$, $\gamma' \in U(N_{i+1})$, and all $N$, $\mathrm{fr}$, $N'$, $\mathrm{fr}'$, $c$ and $x$ such that $N$ and $N'$ are self-dual, $0 < c$, $c \mid D$ and $x$ is in the $D^{-1}$-scaled lattice of maps from $N$ to $N'$,
$$\Theta_i(\gamma N, \gamma\,\mathrm{fr}, \gamma' N', \gamma'\,\mathrm{fr}', c, \gamma' x\gamma^{-1}) = \rho_{i+1}(\gamma')\circ\Theta_i(N, \mathrm{fr}, N', \mathrm{fr}', c, x)\circ\rho_i(\gamma^{-1}).$$

Lean: `Formalism.L2.Ker.Cd.CarC.thEquivP_ambOf_tiesD`

*Proof.* By the last of the ties, the row weights of the word $u$ are the row weights, so $e_\tau$ is also the weight of row $\tau$ of $u$ at level $i$. A general theorem on step distributions gives the equivariance from five facts: the rationality of jets, which is assumed; the condition $E_\Omega$ on $A$, which holds because $B$ is standard; the naturality of the theta coset indicator; the character law of $A$; and the product law at the two ranks $N_i$ and $N_{i+1}$. The ranks $N_i$ and $N_{i+1}$ are even. The naturality of the indicator follows from the conjugation law of $A$, the lattice hypotheses, $D > 0$ (which holds because $u$ has a positive count) and the equality law of $A$, which comes from the curve data. The character law holds for even ranks. The product law at both ranks is [the product law of the local measures](/entry/mu-prod-law-of/) with this $e$. $\square$

### Jets at a split prime

Now let the curve data be of the first kind, with $s$, $\mathfrak{c}$, $\delta$, $B$, $\chi$, $c_D$ and the ambient datum $A$ as before, and let $d$ be the discriminant of the host field. For a finite set $S$ of primes of $E$, self-dual lattices $N$ and $N'$ of ranks $a$ and $b$, a number $c$ and a map $x$, the datum gives a jet $\mathrm{jet}_{S,N,N'}(c, x, m)$ for each monomial $m$ in the variables of the hom space.

**Theorem 6.8.5 (Jets at a split prime).** Assume that $s$ is valid, that $\mathfrak{c}$ is a curve ideal with twelfth root $\delta$, and that $\chi$ is the character of the data. Let $a$ and $b$ be even, $S$ a finite set of primes of $E$, $N$ and $N'$ self-dual lattices of ranks $a$ and $b$, $p \ge 5$ a prime with an isomorphism $\iota : \mathbb{C} \to \mathbb{C}_p$, such that $N$ and $N'$ are standard at $p$, $p$ does not divide the discriminant of $E$, $|\iota(c_D(\tau))| \le 1$ for all $\tau$, $p \nmid d$, and the lattice hypotheses for $A$ hold at $(a, b, S)$. Let $\pi \in \mathbb{C}$ be an integer of the host field with $\pi\bar{\pi} = p$, and let $p_E \in O_E$ with $\tau(p_E) = \pi$ and $\tau(\bar{p}_E) = \bar{\pi}$ for all $\tau$, such that a prime $P$ over $p$ is in $S$ if and only if $p_E \notin P$. Then for $c' > 0$ with $p \nmid c'$, every $x$ in the $c'^{-1}$-scaled lattice of maps from $N$ to $N'$ at $S$, and every monomial $m$,
$$\bigl|\iota\,\sigma_0\bigl(\mathrm{jet}_{S,N,N'}(pc', x, m)\bigr)\bigr|\cdot|\iota(\bar{\pi})|^{\deg m}\cdot|p|^{|T|\,a\,b} \le 1,$$
where $|T|$ is the number of embeddings in the CM type.

Lean: `Formalism.L2.Ker.Test.jetAtSplit_ambOf`

*Proof.* Under the hypotheses on $s$, $\mathfrak{c}$, $\delta$ and $\chi$, there are $a_0 > 0$, $b_0$, $c_0$ and $\lambda \ne 0$ such that the ambient datum is standard for every choice of even ranks, self-dual lattices standard at $p$, and a prime $p \ge 5$ with $p$ prime to the discriminant of $E$ and $|\iota(c_D)| \le 1$. Apply this to $a$, $b$, $N$, $N'$ and $p$. Since $p \ge 5$, $p \ne 2$. Now [the jet bound at a split prime](/entry/jet-at-split/) gives the claim. $\square$

**Remark 6.8.6 (Formalization).** The theorem on the jets lives in the namespace `Test` ([SelfDualLatticeNorms.lean](lean:Formalism/LocalToGlobal/KernelLattices/KernelLocalFactors/SelfDualLatticeNorms.lean#L110)), but it is the result that `GlobalTheory.AtG.jetSplitAmb_holds` restates with no change ([JetTableBoundSplitPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JetTableBoundSplitPrime.lean#L7)). Its proof drops the CM condition and the lattice identity that come with the standard datum (line 120). Two theorems are named `thEquivP_ambOf_tiesD`: the one here, in `Formalism.L2.Ker.Cd.CarC` ([RkEqcar.lean](lean:Formalism/LocalToGlobal/KernelLattices/KernelLocalFactors/RkEqcar.lean#L29)), and one in `Formalism.L2.Ker` with the extra hypotheses `ThIndOfEq` and `NatOk` ([ThEquivPAmbOfTiesD.lean](lean:Formalism/LocalToGlobal/KernelLattices/KernelLocalFactors/ThetaLocalEquivalence/ThEquivPAmbOfTiesD.lean#L158)). The rank `n` in the product law is a free parameter that the proof only passes on ([LocalProductMeasures.lean](lean:Formalism/LocalToGlobal/KernelLattices/KernelLocalFactors/LocalProductMeasures.lean#L539)); the theorem on equivariance calls it twice with the same arguments, once for each rank. The frame of a lattice at a prime is chosen with `Classical.epsilon`. The curve data "of the first kind" are `D7` and those "of the second kind" are `Car`. The predicate `KerStdEx` is defined twice, in `Formalism.L2.Ker` (KerStd.lean, line 105) and in `Formalism.L2.Ker.Cd` (RkVolKerStd.lean, line 163). The text does not unfold `muAtT`, `mUof`, `LawTies`, `Amb.LaHyp`, `Amb.JetsRatDeg`, `jetK` or `stepT`.

## Notes and references

This chapter feeds five results of the volume and one of Volume 14. The admissible entries of Section 4 give [the inert theta admissibility theorem](/entry/inert-theta-admissibility-of-complex-multiplication/). The integrality of the kernels in Section 2 gives [the service row from Artin reciprocity](/entry/serv-h-row-of-artin/). The theta product form of Section 6 gives [the Frobenius conjugation conditions for the adapted kernel datum](/entry/frobenius-conjugation-conditions-adapted-kernel-datum-alt/), and the packages of Section 7 give [the packages at good primes](/entry/good-prime-packages/). The jet bound of this section gives [the jet bound for the ambient datum](/entry/jet-split-amb-holds/), and the equivariance of a step gives [the chain of theta distributions with a character](/entry/ch-th-ok-chi/).

- S. Lang, *Algebra*, revised third edition, Chapter VI, Theorem 6.1 (Hilbert's Theorem 90).
- N. Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions*, second edition, Chapter IV, Section 2 (Dwork's lemma).
- J. Neukirch, *Algebraic Number Theory*, Chapter VII, Section 6 (Hecke characters).
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, Chapter IV (the formal group of an elliptic curve).
- J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II (complex multiplication).
