---
title: Transport of period data
decls:
  - Formalism.BasicNotions.CmpTie.locTied6_F
  - UpperTheory.Lit.Cmp.locTied6
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Transport of period data

Large parts of the Galois row do not work with a fixed construction of the period rings. They work with abstract *period data*: two rings with the operations that $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$ carry, and the axioms that these operations satisfy. A *tie* of such data to a model of the previous section is a pair of isomorphisms that carries each operation to the corresponding operation of the model. The proof has a tie to model 1, and it needs a tie to model 2, where the facts of the next section are proved. This section proves that a tie to model 1 gives a tie to model 2. The argument composes with the isomorphisms of [the comparison theorem](/entry/compat-f/).

We keep the notation of the previous section: $\ell$, $C = \mathbb{C}_\ell$, $G = \mathrm{Gal}(\overline{\mathbb{Q}}_\ell/\mathbb{Q}_\ell)$, the cyclotomic character $\chi$, $A_{\mathrm{inf}}$, $\theta$ and $J = \ker\theta$. Let $\mathbb{Q}_\ell^{\mathrm{ur}} \subset \overline{\mathbb{Q}}_\ell$ be the maximal unramified extension.

**Definition 1.2.1 (Period data).** *Period data* for $\mathbb{Q}_\ell$ consist of the following.

1. Two commutative $\mathbb{Q}_\ell$-algebras $B$ and $B_{\mathrm{dR}}$, with $B$ an algebra over $\mathbb{Q}_\ell^{\mathrm{ur}}$ and $B_{\mathrm{dR}}$ an algebra over $\overline{\mathbb{Q}}_\ell$.
2. Actions of $G$ on $B$ and on $B_{\mathrm{dR}}$ by $\mathbb{Q}_\ell$-algebra automorphisms. On the images of $\mathbb{Q}_\ell^{\mathrm{ur}}$ and $\overline{\mathbb{Q}}_\ell$ they are the Galois action.
3. A $\mathbb{Q}_\ell$-algebra map $\varphi : B \to B$, a $\mathbb{Q}_\ell$-algebra map $\iota : B \to B_{\mathrm{dR}}$, an element $t \in B$ and a character $\chi_B : G \to \mathbb{Q}_\ell^\times$. For each $m$ and each $\ell^m$-th root of unity $\zeta$, and each $g \in G$, there is an integer $a$ with $|\chi_B(g) - a| \le \ell^{-m}$ and $g(\zeta) = \zeta^a$. So $\chi_B$ is the cyclotomic character.
4. For each finite extension $K$ of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$, a structure of period data over $K$ in the sense of the Lean structure `PeriodData`, whose action, $\varphi$, $\iota$, $t$ and character are the restrictions of those above. It includes a filtration $(\mathrm{Fil}^a_K)_{a \in \mathbb{Z}}$ of $B_{\mathrm{dR}}$ by $K$-subspaces. The filtration does not depend on $K$ as a set.
5. A compatible system $(\zeta_m)_{m \ge 0}$ of $\ell^m$-th roots of unity in $\overline{\mathbb{Q}}_\ell$ with $\zeta_0 = 1$, $\zeta_{m+1}^\ell = \zeta_m$ and $\zeta_1 \neq 1$, and for each finite extension $L$ a valuation $v_L$ of $L$ with $v_L(\ell) = 1$ whose ring of integers is the ring of integers of $L$.

**Definition 1.2.2 ($A_{\mathrm{inf}}$ datum).** Let $P$ be period data. An *$A_{\mathrm{inf}}$ datum* for $P$ consists of an isometric action of $G$ on $C$ that extends the action on $\overline{\mathbb{Q}}_\ell$, a compatible action on $\mathcal{O}_{C^\flat}$, a compatible system $(\zeta_n)$ of $\ell^n$-th roots of unity in $\mathcal{O}_C$ that agrees with the system of $P$, the element $\epsilon \in \mathcal{O}_{C^\flat}$ whose components reduce to the $\zeta_n$ modulo $\ell$, and an injective ring map $\iota_A : A_{\mathrm{inf}} \to B$ with the following properties.

1. $\iota_A$ commutes with the actions of $G$ and with $\varphi$.
2. For each $a \in A_{\mathrm{inf}}$, $\iota(\iota_A(a)) \in \mathrm{Fil}^0$. It lies in $\mathrm{Fil}^1$ if and only if $a$ is divisible by $\xi = \sum_{i=0}^{\ell-1} [\epsilon^{1/\ell}]^i$.
3. If $c \in \mathbb{Q}_\ell^{\mathrm{ur}}$ is a root of unity of order $m$ prime to $\ell$, then $\iota_A$ sends the Teichmüller lift of the element of $\mathcal{O}_{C^\flat}$ built from the roots $c^{1/\ell^k}$ of order $m$ to the image of $c$ in $B$.

**Definition 1.2.3 (Tie).** Let $P$ be period data with an $A_{\mathrm{inf}}$ datum $A$, and fix a model $M \in \{1, 2\}$ of the previous section. A *tie* of $(P, A)$ to model $M$ is a pair of ring isomorphisms
$$e_B : B \to B_{\mathrm{cris}}^{(M)}, \qquad e_D : B_{\mathrm{dR}} \to B_{\mathrm{dR}}^{(M)}$$
with the following properties.

1. $e_B$ and $e_D$ send each $z \in \mathbb{Z}_\ell$ to $z$.
2. For each $x \in \overline{\mathbb{Q}}_\ell$, the element $e_D(x)$ lies in $B_{\mathrm{dR}}^+$ and $\theta(e_D(x)) = x$.
3. $e_B$ and $e_D$ commute with the actions of $G$, and $e_B$ commutes with $\varphi$.
4. The map $e_D \circ \iota \circ e_B^{-1}$ is the inclusion of model $M$.
5. For each $K$, each $a$ and each $x \in B_{\mathrm{dR}}$, $x \in \mathrm{Fil}^a_K$ if and only if $e_D(x) \in \mathrm{Fil}^a$.
6. $e_D(\iota(t))$ lies in $B_{\mathrm{dR}}^+$ and is the logarithm of $\epsilon$ in the sense of model $M$.
7. $e_B \circ \iota_A$ is the map $A_{\mathrm{inf}} \to B_{\mathrm{cris}}^{(M)}$ of the model.

A tie identifies the abstract data with a concrete period ring. Results proved from the axioms of $P$ then hold for the concrete ring, and results proved for the concrete ring hold for $P$.

**Theorem 1.2.4 (Transport of ties).** Let $P$ be period data for $\mathbb{Q}_\ell$ and $A$ an $A_{\mathrm{inf}}$ datum for $P$. If $(P, A)$ has a tie to model 1, then it has a tie to model 2.

Lean: `UpperTheory.Lit.Cmp.locTied6` (also `Formalism.BasicNotions.CmpTie.locTied6_F`, the same statement).

*Proof.* Let $(e_B, e_D)$ be a tie to model 1, and let $(e'_B, e'_D, e'_P)$ be the isomorphisms of [the comparison theorem](/entry/compat-f/). We claim that $(e'_B \circ e_B, e'_D \circ e_D)$ is a tie to model 2. We check the seven properties in turn.

1. Both ties and both comparison maps fix $\mathbb{Z}_\ell$.
2. Let $x \in \overline{\mathbb{Q}}_\ell$. By the tie, $e_D(x) = y$ for some $y \in B_{\mathrm{dR}}^{+(1)}$ with $\theta(y) = x$. Then $e'_D(y) = e'_P(y)$ lies in $B_{\mathrm{dR}}^{+(2)}$, and $\theta(e'_P(y)) = \theta(y) = x$.
3. Each of the four maps commutes with $G$, and $e_B$ and $e'_B$ commute with $\varphi$.
4. By the tie, $f = e_D \circ \iota \circ e_B^{-1}$ is the inclusion of model 1. By property 4 of the comparison theorem, $e'_D \circ f \circ e'^{-1}_B$ is the inclusion of model 2. This map is $(e'_D e_D) \circ \iota \circ (e'_B e_B)^{-1}$.
5. Combine property 5 of the tie with property 5 of the comparison theorem.
6. By the tie, $e_D(\iota(t)) = y$ with $y \in B_{\mathrm{dR}}^{+(1)}$ the logarithm of $\epsilon$ in model 1. By property 6 of the comparison theorem, $e'_P(y)$ is the logarithm of $\epsilon$ in model 2, and $e'_D(y) = e'_P(y)$ by property 2.
7. Combine property 7 of the tie with property 7 of the comparison theorem.

Only the existence of the comparison isomorphisms is used, so the theorem follows from [the existence statement](/entry/cmp-f/). $\square$

**Remark 1.2.5.** The proof of the [basic properties of $B_{\mathrm{cris}}$](/entry/period-ring-base-base/) uses this theorem once, in the proof that there is no Kummer period. Other results below [the local steps](/entry/steps-holds/) use it as well, for example in the proof that a piece of the cohomology of a tower is crystalline. The source file of the theorem, [LocalComparisonFromAlternative.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/CrystallineComparison/LocalComparisonFromAlternative.lean#L24), also proves the converse, that a tie to model 2 gives a tie to model 1. The converse is not part of this chapter. We did not unfold the Lean structure `PeriodData` beyond the fields named above.
