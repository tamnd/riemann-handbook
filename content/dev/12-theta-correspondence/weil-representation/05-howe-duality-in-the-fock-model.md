---
title: Howe duality in the Fock model
decls:
  - GlobalTheory.HoweR.fock_pack
  - GlobalTheory.T.howeQuotientFiniteLength_fockPolynomials
  - GlobalTheory.HoweR.howeAlg_tensAny
  - GlobalTheory.T.howe_finite_length_tensor_product_factors
  - GlobalTheory.howeAlg_fock_tensor
  - GlobalTheory.T.howe_duality_characters_fock_tensor_product
  - GlobalTheory.howeDualityReal_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Howe duality in the Fock model

This section proves the archimedean Howe duality statement that the later chapters use for a character of the first group: for a global unitary dual pair over a CM field, the theta submodules of the polynomial Fock space at the infinite places satisfy a bound on the length of chains, and the sum of two proper ones is proper. So the archimedean big theta lift of a character has finite length and a unique irreducible quotient. The statement is [Howe duality at the real places](/entry/howe-duality-real-of-literature/), from R. Howe, *Transcending classical invariant theory*, J. Amer. Math. Soc. 2 (1989). The proof here is algebraic: it works in the [Fock model](/learn/theta/#the-fock-model), where the two Lie algebras act on polynomials, and it uses only [[highest weight|C5W8BE1DRY]] theory for $\mathfrak{gl}$.

### The Fock space of one place

For $p, q \in \mathbb{N}$ let $I_{p,q} = \{1, \dots, p\} \sqcup \{1, \dots, q\}$, and call the first part positive and the second part negative. Let $\mathfrak{gl}_{p,q}$ be the complex matrices indexed by $I_{p,q}$, with matrix units $E_{ab}$.

**Definition 1.5.1 (Fock space).** For $p, q, r, s \in \mathbb{N}$ let $\mathcal{P} = \mathcal{P}(p,q,r,s)$ be the polynomial ring over $\mathbb{C}$ in variables $z_l$, $l = (a, c) \in I_{p,q} \times I_{r,s}$. Call $l$ positive if $a$ and $c$ are both positive or both negative. For positive $l$ put $\uparrow_l = z_l$ and $\downarrow_l = \partial/\partial z_l$; for the other $l$ put $\uparrow_l = -\partial/\partial z_l$ and $\downarrow_l = z_l$. Put $\omega(E_{ll'}) = \uparrow_l \downarrow_{l'} + \tfrac12 \delta_{ll'}$.

**Definition 1.5.2 (The two actions).** The actions $\pi_1$ of $\mathfrak{gl}_{p,q}$ and $\pi_2$ of $\mathfrak{gl}_{r,s}$ on $\mathcal{P}$ are
$$\pi_1(E_{ab}) = \sum_{c \in I_{r,s}} \omega(E_{(a,c),(b,c)}), \qquad \pi_2(E_{cd}) = \sum_{a \in I_{p,q}} \omega(E_{(a,c),(a,d)}).$$
For $x \in \mathbb{C}$ the *coinvariant space* is
$$C_x = \operatorname{span}\{\pi_1(Z)f - x \operatorname{tr}(Z) f : Z \in \mathfrak{gl}_{p,q},\ f \in \mathcal{P}\}.$$

These are the complexified [[Lie algebra|5JJYBJ6A8K]] actions of $\mathrm{U}(p,q)$ and $\mathrm{U}(r,s)$ in the oscillator representation of $\mathfrak{u}(pr+qs, ps+qr)$, after the [[Bargmann transform|QPH28QH036]]. The two actions commute, and $\mathcal{P}/C_x$ is the space of coinvariants of $\mathfrak{gl}_{p,q}$ for the character $x \operatorname{tr}$, as a module for $\mathfrak{gl}_{r,s}$.

For a linear action $a$ of $\mathfrak{gl}_{r,s}$ on a space $V$, a vector $v$ is a *highest weight vector of weight* $\mu \in \mathbb{Q}^{I_{r,s}}$ if $a(E_{cc})v = \mu_c v$ for all $c$ and $a(E_{cd})v = 0$ for the positive roots $E_{cd}$. A subspace $N$ is *stable* if $a(Z)N \subset N$ for all $Z$.

**Definition 1.5.3 (Howe package).** Let $a$ be an action of $\mathfrak{gl}_{r,s}$ on $V$ and $C \subset V$ a subspace. The pair $(a, C)$ is a *Howe package* if:

1. $a$ is a Lie algebra map, $V$ is the sum of its weight spaces with rational weights, and each finite subset of $V$ lies in a finite dimensional space on which the block diagonal part of $\mathfrak{gl}_{r,s}$ acts and is unitary for some inner product;
2. $C$ is stable;
3. there are $\alpha, \beta, \alpha', \beta' \in \mathbb{C}$ such that, for all $c, d$ and all $v \in V$, the quadratic expression $\sum_e a(E_{ce})a(E_{ed})v - \alpha\, a(E_{cd})v - \delta_{cd}\beta v$ lies in $C$, and the same holds for the action $Z \mapsto -a({}^tZ)$ with $\alpha', \beta'$;
4. for each bound $B$ there is a finite dimensional $U \subset V$ that contains, modulo $C$, all highest weight vectors whose weights have entries of absolute value at most $B$;
5. there are $\mu$ and a highest weight vector $v$ of weight $\mu$ that generates $V$ modulo $C$, and each highest weight vector of weight $\mu$ lies in $\mathbb{C}v + C$.

**Theorem 1.5.4 (The Fock space is a Howe package).** For all $p, q, r, s$ and $x \in \mathbb{C}$, the pair $(\pi_2, C_x)$ on $\mathcal{P}(p,q,r,s)$ is a Howe package.

Lean: `GlobalTheory.HoweR.fock_pack` (also `GlobalTheory.T.howeQuotientFiniteLength_fockPolynomials`, a second name).

*Proof.* The theorem collects five facts about the Fock space. First, $\pi_1$ and $\pi_2$ are Lie algebra maps that commute, and the monomials are weight vectors with integral weights. Second, $C_x$ is stable under $\pi_2$, since $\pi_2$ commutes with $\pi_1$ and with scalars. Third, the Fock inner product, for which the monomials are orthogonal, makes $\uparrow_l$ and $\downarrow_l$ adjoint up to sign; so the block diagonal part of $\pi_2$ acts unitarily on the finite dimensional spaces of polynomials of bounded degree. Fourth, the quadratic identities modulo $C_x$ come from an identity of Capelli type in the Fock space, which writes $\sum_e \pi_2(E_{ce})\pi_2(E_{ed})$ in terms of $\pi_2(E_{cd})$, the scalar $\delta_{cd}$ and the image of $\pi_1$; modulo $C_x$ the operators $\pi_1(Z)$ act by the scalar $x\operatorname{tr}(Z)$. Fifth, admissibility and the cyclic highest weight vector of multiplicity one are the highest weight theory of the coinvariant module, as in [highest weights and branching](/learn/representations/#highest-weights-and-branching). $\square$

### Tensor products and the algebraic theorem

Let $T$ be a finite set and, for each $w \in T$, let $a_w$ be an action of $\mathfrak{gl}_{r_w, s_w}$ on $V_w$ and $C_w \subset V_w$. On $V = \bigotimes_w V_w$ let $a_w$ act on the factor $w$. Let $C_{\mathrm{any}} \subset V$ be the span of the pure tensors $\otimes_w v_w$ with $v_{w'} \in C_{w'}$ for at least one $w'$, so $V / C_{\mathrm{any}} = \bigotimes_w V_w/C_w$.

**Definition 1.5.5 (Howe property).** The family $(a_w)$ and a subspace $C \subset V$ have the *Howe property* if there is $L$ such that each strictly increasing chain $N_1 \subsetneq \dots \subsetneq N_m$ of subspaces that are stable under all $a_w$ and contain $C$ has $m \leq L$, and if for any two such subspaces $N, N' \neq V$ one has $N + N' \neq V$.

The second condition says that $V/C$ has a unique maximal proper submodule, so a unique irreducible quotient.

**Proposition 1.5.6 (Cyclic highest weight criterion).** Let $(a_w)$ be commuting actions on $V$, each as in condition 1 of a Howe package, and let $C \subset V$. Suppose that the quadratic relations 3 hold modulo $C$ for each $w$, that the admissibility 4 holds for the joint highest weights, and that there is a joint highest weight vector $v$ of weight $\mu = (\mu_w)$ that generates $V$ modulo $C$ and spans the joint highest weight vectors of weight $\mu$ modulo $C$. Then $(a_w)$ and $C$ have the Howe property.

*Proof.* For the second condition, let $N \neq V$ be stable with $C \subset N$. Then $v \notin N$, since $v$ generates $V$ modulo $C$. All weights of $V/C$ are at most $\mu$, since $V/C$ is generated by a vector of weight $\mu$, and the weight space of weight $\mu$ in $V/C$ is spanned by the image of $v$. A stable subspace is the sum of its weight spaces, so the $\mu$ component of $N$ lies in $C$. The same holds for $N'$, so the $\mu$ component of $N + N'$ lies in $C$, and $v \notin N + N'$.

For the bound on chains, each nonzero subquotient $N_{k+1}/N_k$ has a joint highest weight vector, since the weights are rational and bounded above by $\mu$. Applied to a highest weight vector, the quadratic relations 3 become polynomial equations in the entries of its weight; with the relations for the negative transpose they bound the entries by some $B$. By admissibility, the highest weight vectors that occur lie in $U + C$ with $\dim U < \infty$, and each step of the chain needs a new direction in $U$. So $m \leq \dim U + 1$. $\square$

**Theorem 1.5.7 (Tensor products of Howe packages).** If $(a_w, C_w)$ is a Howe package for each $w \in T$, then $(a_w)$ on $\bigotimes_w V_w$ and $C_{\mathrm{any}}$ have the Howe property.

Lean: `GlobalTheory.HoweR.howeAlg_tensAny` (also `GlobalTheory.T.howe_finite_length_tensor_product_factors`, a second name).

*Proof.* The actions on different factors commute, and the conditions of 1 pass to the tensor product. The quadratic relations for $a_w$ hold modulo $C_w$ in the factor $w$, so modulo $C_{\mathrm{any}}$ in $V$. A joint highest weight vector of weight $(\mu_w)$ lies in the span of the pure tensors of highest weight vectors of weight $\mu_w$; so admissibility follows from that of each factor, with $U = \bigotimes_w U_w$. The pure tensor $\otimes_w v_w$ of the cyclic vectors is a joint highest weight vector, it generates $V$ modulo $C_{\mathrm{any}}$, and the joint highest weight vectors of its weight lie in $\mathbb{C}\, {\otimes_w v_w} + C_{\mathrm{any}}$. The cyclic highest weight criterion gives the claim. $\square$

**Corollary 1.5.8 (Algebraic Howe duality for characters).** For a finite set $T$, numbers $p_w, q_w, r_w, s_w$ and $x_w \in \mathbb{C}$, the actions $\pi_{2,w}$ on $\bigotimes_w \mathcal{P}(p_w, q_w, r_w, s_w)$ and the subspace $C_{\mathrm{any}}$ built from the $C_{x_w}$ have the Howe property.

Lean: `GlobalTheory.howeAlg_fock_tensor` (also `GlobalTheory.T.howe_duality_characters_fock_tensor_product`, a second name).

*Proof.* Each factor is a Howe package by the first theorem, and the tensor product theorem applies. $\square$

### The global statement

Let $F$ be a totally real field and $E/F$ a CM extension with complex conjugation $\sigma$. Let $X$ be a nondegenerate Hermitian space of dimension $n$ and $W$ a nondegenerate skew-Hermitian space of dimension $d$ over $E$, with a Weil representation $\omega$ of $\mathrm{U}(X) \times \mathrm{U}(W)$ over the adeles, for a standard character $\psi$ of $\mathbb{A}_F / F$ and splitting characters $\chi_X, \chi_W$. For each infinite place $w$ choose an embedding of $E$ over $w$ and Cartan involutions of $X$ and $W$ at $w$. Let $\mathcal{P}_\infty$ be the space of polynomial Fock vectors in the archimedean Schwartz space.

**Definition 1.5.9 (Theta submodule).** A subspace $N \subset \mathcal{P}_\infty$ is a *theta submodule* if it contains $Y f$ and $k f - f$ for all $f \in \mathcal{P}_\infty$, all $Y$ in the Lie algebra of $\mathrm{U}(X)_\infty$ and all $k$ in the maximal compact subgroup of $\mathrm{U}(X)_\infty$, and it is stable under the Lie algebra and the maximal compact subgroup of $\mathrm{U}(W)_\infty$.

So $\mathcal{P}_\infty / N$ is a quotient of the coinvariants of $\mathrm{U}(X)_\infty$ for the trivial character, as a module for $\mathrm{U}(W)_\infty$.

**Theorem 1.5.10 (Howe duality at the real places).** In this setting there is $L$ such that each strictly increasing chain of theta submodules has length at most $L$, and if $N, N'$ are theta submodules different from $\mathcal{P}_\infty$, then $N + N' \neq \mathcal{P}_\infty$.

Lean: `GlobalTheory.howeDualityReal_holds`.

This is the case of a character of [the local theta correspondence](/learn/theta/#the-local-theta-correspondence) of Volume 1, in the form of R. Howe, *Transcending classical invariant theory*, J. Amer. Math. Soc. 2 (1989), Theorem 2.1: for a real reductive dual pair $(G, G')$ and an irreducible Harish-Chandra module $\pi$ of $G$ that is a quotient of the oscillator representation, the maximal $\pi$-isotypic quotient is $\pi \otimes \Theta(\pi)$, where $\Theta(\pi)$ has finite length and a unique irreducible quotient.

*Proof.* At each infinite place $w$ the Hermitian space $X$ has a signature $(p_w, q_w)$ and $W$, after multiplication by $i$, a signature $(r_w, s_w)$. Frames adapted to the Cartan involutions give an injective linear map
$$\Phi \colon \bigotimes_w \mathcal{P}(p_w, q_w, r_w, s_w) \to \mathcal{P}_\infty$$
with image $\mathcal{P}_\infty$, and constants $c_w, c'_w$, such that the Lie algebra of $\mathrm{U}(X)$ at $w$ acts through $\pi_{1,w}$ shifted by $c_w \operatorname{tr}$ and that of $\mathrm{U}(W)$ through $\pi_{2,w}$ shifted by $c'_w \operatorname{tr}$. The shifts come from the splitting characters.

For a theta submodule $N$, the preimage $\Phi^{-1}(N)$ is stable under each $\pi_{2,w}$, and it contains $C_{\mathrm{any}}$ built from the $C_{-c_w}$, since $N$ contains $Yf$ for all $Y$ in the Lie algebra of $\mathrm{U}(X)_\infty$. Since $\Phi$ is a bijection onto $\mathcal{P}_\infty$, one has $\Phi(\Phi^{-1}(N)) = N$, so $\Phi^{-1}$ keeps strict inclusions and proper subspaces, and $\Phi^{-1}(N) + \Phi^{-1}(N') = \Phi^{-1}(N + N')$. The corollary on algebraic Howe duality, with $x_w = -c_w$, gives both claims. $\square$

**Remark 1.5.11.** Only the coinvariants of a character of the first group occur, and the conclusion is about the second group. This is the half of Howe duality that the theta lift of a character needs: it gives a unique irreducible quotient of the archimedean big theta lift, but it does not prove that the correspondence is a bijection.

**Remark 1.5.12 (Formalization).** The five facts in the proof of the first theorem rest on six results, `fockActions_lie_rationalWeights_commute`, `fockCoinvariantKernel_stable_and_admissible`, `fockSecondAction_quadraticIdentity_mod_coinvariants`, `negTranspose_fockSecondAction_quadratic_mod_coinvariants`, `fockAction_isLocallyBlockUnitary` and `fockCoinvariants_highestWeightCyclic_multiplicityOne` in `GlobalTheory.T`; we have not opened their proofs, so the account of them above is ours. The criterion is `GlobalTheory.T.howeAlg_of_cyclic_highest_weight` (HoweFiniteLengthUniqueMaximalOfCyclicStatement.lean, line 7), and the proof of it above is our sketch. The package is `Pack` and the Howe property is `HoweAlg` (Definitions/Divisors/ActAtApply.lean, lines 58 and 84). The Fock space and its operators live in Formalism/LocalRingCardinality/DataTheta.lean (lines 182 to 212) under the namespace `Formalism.BasicNotions.TH`; the file path does not match the content. In `GlobalTheory.howeDualityReal_holds` (HoweDualityRealHolds.lean, line 19), the hypotheses `ResEtaPow` and `IsHecke` on $\chi_X$ and $\chi_W$ are bound as `_` and never used, and the first clause of the frame data is dropped. The second names are `first | exact ...` wrappers under `maxHeartbeats 1000000` (the three Statement files, line 6 of each).
