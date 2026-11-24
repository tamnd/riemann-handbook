---
title: From U(2) to U(3) and adjoint automorphy
decls:
  - UpperTheory.V.Z.Sym.So.specF
  - UpperTheory.V.Z.Sym.Dict.Br.bridgeEx
  - core
  - UpperTheory.V.Z.Sym.W.specOutS
  - UpperTheory.V.Z.Sym.W.adjoint_lift_w_of_literal_automorphy_spec_out
  - UpperTheory.V.Z.Sym.W.core
  - UpperTheory.V.Z.Sym.W.adjoint_automorphy_w_of_pure_weight_adjoint_lift
  - UpperTheory.V.Z.Sym.W.adjoint_automorphy_w_of_printed_hida_window
status: drafted
drafted_by: writer@claude-opus-5-5
---
## From U(2) to U(3) and adjoint automorphy

This section uses [the trace identity](/entry/t-fid0/) to move automorphic forms from a definite $U(2)$ to a definite $U(3)$. The output is a dichotomy: an eigenform on $U(2)$ with parameters $a$ gives an eigenform on $U(3)$ with parameters $(a, 1, a^{-1})$, or an eigenform on $U(2)$ with parameters $a^2$. From it we get the adjoint lift, and from the adjoint lift the automorphy of $\operatorname{ad}^0 r$ for the two-dimensional representations $r$ that the three-dimensional unitary case needs. We keep the notation of the previous section for $F$, $\Delta$, $E$, $U_3$, $D^\times$, $D^1$, the transfer data and the cone.

**Definition 8.13.1 (Eigen conditions).** Let $a = (a_v)_{v \in \Sigma}$ be characters of $F_v^\times$. For $t$ in the cone put $\mathrm{ex}(a, t) = \prod_{v \in \Sigma} \delta^{-1/2}(t_v, t_v^{-1})\, a_v(t_v)$, where $\delta$ is the modulus character of the Borel subgroup. A form on $D^1$ satisfies the eigen condition for $a$ if, for each $t$ in the cone, the double coset of $\operatorname{diag}(t, t^{-1})$ acts on it by $\mathrm{ex}(a, t)$. The eigen condition for $a$ on $U_3$ is the same for all dominant diagonal elements, with the character $(a_v, 1, a_v^{-1})$. On $D^\times$ it is the same as on $D^1$, at the level of $D^\times$.

**Theorem 8.13.2 (Dichotomy over a totally real field).** Let the transfer data be valid. Let $x$ be a finite adele of $D^\times$ that is 1 at $\Sigma$, and let $B_G$, $B_S$ (at $x$) and $B_K$ be spaces of forms with finite dimensional weights that share a trace function $c$. Let $\varphi \ne 0$ in $B_S$ satisfy the eigen condition for $a$. Then $B_G$ has a nonzero form with the eigen condition for $a$, or $B_K$ has a nonzero form with the eigen condition for $a^2$.

Lean: `UpperTheory.V.Z.Sym.So.specF`.

*Proof.* The trace identity at $x$ gives $x_0 = x, x_1, \dots, x_n$, $a_1 > 0$ and $b$ with
$$\operatorname{tr} R_\theta(f_G^t) = a_1 \sum_i \operatorname{tr} R(f_S^{t,x_i}) + b \operatorname{tr} R(f_K^t)$$
on the cone. All spaces are finite dimensional. On each side, $t \mapsto R(f^t)$ is multiplicative on the cone, so each trace is a finite sum of characters of the cone. On the $U_3$ side, a character $\beta$ that occurs with a nonzero coefficient and equals $\mathrm{ex}(a, \cdot)$ gives a nonzero form with the eigen condition for $a$. On $D^1$, $\varphi$ is an eigenvector with character $\mathrm{ex}(a, \cdot)$. On $D^\times$, an eigenvector with this character satisfies the eigen condition for $a^2$. Now characters of a commutative semigroup are linearly independent (S. Lang, *Algebra*, Chapter VI, Theorem 4.1). Since $a_1 > 0$ and the $D^1$ traces have nonnegative multiplicities, the character $\mathrm{ex}(a, \cdot) \ne 0$ occurs on the left side or in the $D^\times$ trace. $\square$

To use the dichotomy for a CM field $L$, we write $L$ as a quadratic extension of its totally real subfield $L^+$.

**Proposition 8.13.3 (Bridges).** Let $L$ be a CM field that is unramified over $L^+$ at all finite places. Then there is a bridge for $L$: a totally negative $\Delta \in L^+$ with $L \cong L^+(\sqrt{\Delta})$, isomorphisms that identify $U(3)$ over $L$ with $U_3$ and $SU(2)$ over $L$ with $D^1$, local splittings at the split places, matching characters, and the compatibility of levels, conjugation and integral structures.

Lean: `UpperTheory.V.Z.Sym.Dict.Br.bridgeEx`.

*Proof.* Choose $\Delta$ with $L = L^+(\sqrt{\Delta})$ and fix the embeddings at each place. This gives ring maps at each place, and the matrix groups are then matched entry by entry. At a split place $w$ the local splitting is an isomorphism $L_w \cong L^+_v$ that respects valuations, absolute values and the standard compact subgroups. $\square$

For $n = 2, 3$ let $K_n$ be the product of the groups $\mathrm{GL}_n(\mathcal{O}_w)$. For a finite set $S$ of places of $L$ and local levels $V_w$, let $\mathrm{lev}(U, S, V)$ be $U$ cut down at each $w \in S$ to an Iwahori type group. The level $\mathrm{iw}$ has depth 0, and the level $\mathrm{deep}(c)$ has diagonal entries in $1 + \varpi^{c+1}\mathcal{O}_w$. The eigen conditions on $U(2)$ and $U(3)$ over $L$ are those above, at places of $L$.

**Lemma 8.13.4 (Transfer at one level).** Fix a bridge for $L$. Let $S$ be a finite set of places with local levels $V$, and let transfer data over $L^+$ fit $(S, V)$. Let $j \ge 1$, and let $\varphi \ne 0$ be a form on $U(2)$ of weight $\mathrm{Sym}^j \otimes {\det}^e$ and level $\mathrm{lev}(K_2, S, V)$ with the eigen condition for $a$ on $S$. Then there is a nonzero form on $U(3)$ of level $\mathrm{lev}(K_3, S, V)$ with the eigen condition for $(a, 1, a^{-1})$, or a nonzero form on $D^\times$ of weight $\mathrm{Sym}^{2j+1}$ with the eigen condition for $b^2$, where $b$ matches $a$ under the splittings.

Lean: `core`.

*Proof.* Move $\varphi$ to $D^1$ at a suitable adele $y$, trivial at the places of the data; it keeps the eigen condition for $b$. Apply the dichotomy over $L^+$. In the first case, move the form on $U_3$ back to $U(3)$ over $L$. $\square$

**Theorem 8.13.5 (Transfer from U(2) to U(3)).** Let $S_0$ be a finite set of split places of $L$, at most one above each place of $L^+$, with a place above each place of $L^+$ over 2. Let $j \ge 1$. There is $c_0$ such that for each $c \ge c_0$ there is an open subgroup $U_2 \subseteq K_2$ with this property. Let $S_1$ be disjoint from $S_0$, such that $S_0 \cup S_1$ has the properties of $S_0$. Let $\varphi \ne 0$ be a form of weight $\mathrm{Sym}^j \otimes {\det}^e$ and level $\mathrm{lev}(\mathrm{lev}(K_2, S_0, \mathrm{deep}(c)), S_1, \mathrm{iw})$ with the eigen condition for $a_w$ on $S_0 \cup S_1$. Then there is a nonzero form on $U(3)$ of the same level with the eigen condition for $(a_w, 1, a_w^{-1})$ on $S_0 \cup S_1$, or a nonzero form on $U(2)$ of weight $\mathrm{Sym}^{2j+1}$ and level $\mathrm{lev}(U_2, S_1, \mathrm{iw})$ with the eigen condition for $a_w^2$ on $S_1$.

Lean: `UpperTheory.V.Z.Sym.W.specOutS`.

*Proof.* Take a bridge, and take $c_0 = 0$. Choose transfer data over $L^+$ that fit $S_0$ with $\mathrm{deep}(c)$, and a finite set of double coset representatives. Let $U_2$ be a principal congruence subgroup of level at least 3 inside the levels of these representatives. Given $S_1$ and $\varphi$, extend the data to $S = S_0 \cup S_1$ and apply the transfer at one level. In the second case, the form on $D^\times$ moves back to $U(2)$ over $L$ at level $\mathrm{lev}(U_2, S_1, \mathrm{iw})$. $\square$

**Definition 8.13.6 (Adjoint lift).** The adjoint lift property says: let $\pi$ be an automorphic representation of a definite $U(2)$ over $L$ with weight gap $j$ and local characters $\psi_w = (\psi_{w,0}, \psi_{w,1})$ on a set $S_0 \cup P$. Then there is an automorphic $\sigma$ on $U(3)$ whose components at these places have the characters $(\psi_{w,0}/\psi_{w,1}, 1, \psi_{w,1}/\psi_{w,0})$, or an automorphic $\sigma'$ on $U(2)$ whose components have the squared ratios.

**Theorem 8.13.7 (Adjoint lift).** Assume the rank $n$ package. Then the transfer from $U(2)$ to $U(3)$ implies the adjoint lift property.

Lean: `UpperTheory.V.Z.Sym.W.adjoint_lift_w_of_literal_automorphy_spec_out`.

*Proof.* Take $c_0$ from the transfer and a depth $c \ge c_0$ at which the characters $\psi_w$ are trivial on $1 + \varpi^{c+1}\mathcal{O}_w$. The rank $n$ package shows that the forms of the relevant weight on $U(3)$ at level $\mathrm{lev}(K_3, S_0, \mathrm{deep}(c))$, and on $U(2)$ at level $U_2$, give finite sets $A_3$ and $A_2$ of automorphic representations. For each finite $S_1 \subseteq P$, a vector of $\pi$ at the right level satisfies the eigen condition, and the transfer gives an element of $A_3$ or of $A_2$ with the required components on $S_1$. As $A_3 \cup A_2$ is finite and the finite subsets of $P$ are directed, one element works for all $S_1$, so for all of $P$. $\square$

Let $r \colon G_L \to \mathrm{GL}_2(\overline{\mathbb{Q}}_l)$ be continuous, irreducible and attached to a form on $U(2)$, unramified outside a level $M$ with $l \mid M$. Pure weight compatibility is the set of local results that we need about $r$: the Galois representations of unitary forms, compatibility at each place, the local behaviour above $l$ and away from $l$, and descent from $\mathrm{GL}_3$ to $U(3)$.

**Lemma 8.13.8 (Adjoint automorphy at one place).** Assume pure weight compatibility and the adjoint lift property. Let $w_0$ be a finite place with $w_0 \mid M$. Then there is a regular algebraic cuspidal $\pi$ of $\mathrm{GL}_3(\mathbb{A}_L)$ with $\pi^\vee \cong \pi^c$, attached to $\operatorname{ad}^0 r \otimes \varepsilon^{-1}$, with Satake parameters given by $r$ at each $w \nmid M$, and with the correct local type at $w_0$.

Lean: `UpperTheory.V.Z.Sym.W.core`.

*Proof.* Let $\sigma$ be the form on $U(2)$ attached to $r$. Choose a finite set of split places prime to $M$ whose Frobenius elements avoid the bad set of $r$. The local results give the characters $\psi_w$ at these places, at the places above $l$, and at the other places. The adjoint lift gives a form on $U(3)$ or a form on $U(2)$ with squared characters. The second case is impossible: squared ratios cannot occur for an irreducible $r$ with these Frobenius elements. In the first case, base change from $U(3)$ to $\mathrm{GL}_3$ gives $\pi$, and the local result at $w_0$ gives its type. $\square$

**Theorem 8.13.9 (Adjoint automorphy).** Assume pure weight compatibility and the adjoint lift property. Then for each $r$ as above, $\operatorname{ad}^0 r \otimes \varepsilon^{-1}$ is automorphic: there is one regular algebraic conjugate self-dual cuspidal $\pi$ of $\mathrm{GL}_3(\mathbb{A}_L)$ attached to it with the correct local type at every place. Under the extended hypotheses and the Galois row, pure weight compatibility holds, so the conclusion holds.

Lean: `UpperTheory.V.Z.Sym.W.adjoint_automorphy_w_of_pure_weight_adjoint_lift` (also `UpperTheory.V.Z.Sym.W.adjoint_automorphy_w_of_printed_hida_window`, the form with the extended hypotheses).

*Proof.* Take a place $w_1 \mid l$ and the $\pi$ of the lemma at $w_1$. At $w \nmid M$ its type is given by the Satake parameters. At $w \mid M$, the lemma at $w$ gives a representation with the correct type at $w$, and the gluing result of pure weight compatibility moves this type to $\pi$. For the second statement, the extended hypotheses give the classical theorems, the Galois representations of unitary forms and descent, and the Galois row gives compatibility at each place. The transfer from $U(2)$ to $U(3)$ and the adjoint lift theorem give the adjoint lift property. $\square$

**Remark 8.13.10 (Formalization).** Two declarations are named `UpperTheory.V.Z.Sym.W.core`: the private lemma in DenseThresholdCases/MemOfUnder.lean, line 35, and a theorem in WeilDeligneUnramified/MemOfUnder.lean, line 38. The transfer at one level is a private theorem named `core` with no namespace, in [LevUnion.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/WeilDeligneUnramified/LevUnion.lean#L98). The proof of the transfer takes $c_0 = 0$, so every depth works, and $U_2$ depends on $c$, $S_0$ and $j$ only. The dichotomy uses only $a_1 > 0$; the constant $b$ has no sign condition. The bridge theorem is in [BridgeEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GeneralizedEigenspaces/GlobalRationalGL/IntegralConjugation/BridgeEx.lean#L77). The adjoint lift proof ends with a private pigeonhole lemma in [MemLevelOfLocalDepth.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/MemLevelOfLocalDepth.lean#L128).
