---
title: The key invariant
decls:
  - GlobalTheory.KaExists.kaSt
  - GlobalTheory.T.exists_integralKeyInvariantRule_charZero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The key invariant

This section puts the results of the chapter together. To every key input $x$ over an algebraically closed field of characteristic $0$ it attaches a unit $\kappa(x)$, the key invariant, and it proves four properties: a transformation law under a change of the theta section and of the tangent basis, compatibility with extensions of fields, integrality over discrete valuation rings where a fixed integer $M$ is a unit, and holomorphy in the period matrix over $\mathbb{C}$. The integer $M$ can be chosen prime to any given prime $p$. The result is used in [the key rule for half characteristics](/entry/exists-key-rule-char-half/), where the invariants for several primes are put together and normalized. The background is in [the complex uniformization](/learn/abelian-varieties/#the-complex-uniformization), in [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures) and in [completion](/learn/commutative-algebra/#completion).

A key input is $x = (A, L, r, \theta, v)$, as in [the section on the Koszul complex](/entry/koszul-sections-exact-field/). We change only the theta section and the tangent basis: for a scalar $a$ and a matrix $m = (m_{ik})$, the key input $x' = (A, L, r, \theta', v')$ with $\theta' = a\theta$ and $v'_i = \sum_k m_{ik} v_k$ is *obtained from* $x$ *by* $(a, m)$.

**Definition 2.9.1 (Normal key inputs over the complex numbers).** Let $x$ be a key input over $\mathbb{C}$ of dimension $g$, let $\tau, m \in M_g(\mathbb{C})$, $a, b \in \mathbb{C}^g$ and $c \in \mathbb{C}$. Then $x$ is *normal at* $(\tau, m, a, b, c)$ if there is a uniformization $u : \mathbb{C}^g \to A(\mathbb{C})$ such that $\tau$ is symmetric with $\operatorname{Im}\tau$ positive definite, the kernel of $u$ is $\mathbb{Z}^g + \tau\mathbb{Z}^g$, $u$ is compatible with $r$, the section $\theta$ corresponds to the function $c\,\theta[a; b](\tau, \cdot)$, and $v_i$ corresponds to the constant vector field $(2\pi i)^{-1} m_i$, where $m_i$ is the $i$-th row of $m$. The pair $(a, b)$ is a *half characteristic* if each $a_i$ and each $b_i$ is $0$ or $\tfrac12$.

Lean: `GlobalTheory.KeyPow.NormalAt`, `GlobalTheory.KeyPow.charHalf`.

For $m = 1$ and $c = 1$ this is the theta witness of [the section on holomorphy](/entry/ka-val-locally-holomorphic/).

**Definition 2.9.2 (Key invariant rules).** Let $g, c, M \geq 1$. A *key invariant rule* of dimension $g$, weight $c$ and level $M$ is a choice of a unit $\kappa(x) \in K^\times$ for every algebraically closed field $K$ of characteristic $0$ and every key input $x$ over $K$, with the following four properties for every $x$ of dimension $g$.

1. *Weight.* If $x'$ is obtained from $x$ by $(a, m)$, with $a \in K$ and $m \in M_g(K)$, then $a^{8c}\kappa(x') = \det(m)^{4c}\kappa(x)$.
2. *Base change.* If $f : K \to K'$ is a homomorphism of algebraically closed fields of characteristic $0$ and $x'$ is a pullback of $x$ along $f$, then $\kappa(x') = f(\kappa(x))$.
3. *Integrality.* If $x$ is a key input over a discrete valuation ring $R$ of characteristic $0$ in which $M$ is a unit, then there are a discrete valuation ring $R'$, an injective local homomorphism $j : R \to R'$ and a unit $u \in R'^\times$ such that $\kappa(x_K) = f(u)$ for every algebraically closed field $K$ of characteristic $0$, every homomorphism $f : R' \to K$ and every pullback $x_K$ of $x$ along $f \circ j$.
4. *Holomorphy.* For every half characteristic $(a, b)$ there is a function $U$ on $M_g(\mathbb{C})$, holomorphic on the Siegel space, such that $\kappa(x) = U(\tau)$ for every key input $x$ over $\mathbb{C}$ that is normal at $(\tau, 1, a, b, 1)$.

The *key invariant statement* says: for every $g \geq 1$ and every prime $p$ there are $c, M \geq 1$ with $p \nmid M$ and a key invariant rule of dimension $g$, weight $c$ and level $M$.

Lean: `GlobalTheory.KeyKa.KaRule`, `GlobalTheory.KeyKa.KaSt`.

For $a = 1$ the weight law reads $\kappa(x') = \det(m)^{4c}\kappa(x)$. In the integrality property $f$ need not be injective: if the residue field of $R'$ has characteristic $0$, it covers the special fibre as well as the generic fibre.

We use four hypotheses besides the laws. The *uniformization theorem* is the one of [the section on holomorphy](/entry/ka-val-locally-holomorphic/). The *algebraicity of tori* says that for every $\tau$ in the Siegel space and every half characteristic $(a, b)$ there are a principally polarized abelian variety over $\mathbb{C}$ with a uniformization of kernel $\mathbb{Z}^g + \tau\mathbb{Z}^g$ and a section of $L$ that corresponds to $\theta[a; b](\tau, \cdot)$, such that tangent vectors are constant vector fields, sections of $L^n$ are the theta functions of level $n$ with characteristic $(a, b)$, $L^N$ is very ample for $N \geq 3$, and linear maps that preserve the lattice come from endomorphisms. *Descent to countable fields* says that every key input over a field $K$ of characteristic $0$ is a pullback of a key input over a countable subfield of $K$. From these two, every $\tau$ in the Siegel space and every half characteristic give a key input over $\mathbb{C}$ that is normal at $(\tau, 1, a, b, 1)$.

**Lemma 2.9.3 (Numerical data).** Let $g \geq 1$ and let $p$ be a prime. There is admissible data $(n, l, l', \alpha)$ for $g$ such that $P = \prod_{j=0}^{g}(l - jn)(l' - jn)$ is prime to $p$, and $P \geq 1$ and $c = 2P^{3g+2}\, g!\, n^g (l' - l) \geq 1$.

Lean: `GlobalTheory.KeyKa.exists_admissibleKeyNumericalData_prime_to`.

*Proof.* Take $n = 4p$, $l = 4pg + 1$ and $l' = l + p$. Then $n \geq 4$ and $gn < l < l'$. For $0 \leq j \leq g$ we have $l - jn = 4p(g - j) + 1$ and $l' - jn = p(4(g - j) + 1) + 1$, both $\equiv 1 \pmod p$, so $p \nmid P$ and $P \geq 1$. For $\alpha$, write $m = a_0^2 + a_1^2 + a_2^2 + a_3^2$ by Lagrange's theorem and let $\alpha(m)$ be the matrix of left multiplication by the quaternion $q = a_0 + a_1 i + a_2 j + a_3 k$ in the basis $1, i, j, k$. Since $|qy| = |q|\,|y|$, we get $\alpha(m)^{T}\alpha(m) = m$. Finally $c \geq 1$ since $l' - l = p \geq 1$. $\square$

**Lemma 2.9.4 (Key values over a discrete valuation ring).** Assume the laws. Let $R$ be a discrete valuation ring, let $x$ be a key input over $R$ of dimension $g$ and let $(n, l, l', \alpha)$ be admissible for $g$, with $P$ a unit in $R$. Then there are a discrete valuation ring $R'$, an injective local homomorphism $j : R \to R'$, a pullback $x'$ of $x$ along $j$, sections $s'$ of $L'^n$ and a key value $u \in R'^\times$ of $s'$.

Lean: `GlobalTheory.KaExists.exists_kaVal_dvr`.

*Proof.* Let $k$ be the residue field of $R$, let $\Omega$ be the algebraic closure of $k(T_q : q \in I)$, for $I = \{1, \dots, g\} \times \{1, \dots, n^g\}$, and let $r : R \to \Omega$ be the residue map. Then $T$ is algebraically independent over $k$. There are a complete discrete valuation ring $O$, an injective local homomorphism $j : R \to O$ and $r' : O \to \Omega$ with $r' \circ j = r$ and kernel the maximal ideal, such that every $T_q$ is $r'(T'_q)$ for some $T'_q \in O$. Let $b$ be a basis of $\Gamma(A, L^n)$ over $R$, let $x_O$ be a pullback of $x$ to $O$, and let $s$ be the sections of $x_O$ with coordinates $T'$ in the pulled back basis. Their pullbacks to $\Omega$ have coordinates $T$, which are algebraically independent over $k$, in a basis that comes from the key input over $k$. So they meet transversally. Since $P$ is a unit in $O$, the existence of a key value after an extension of the discrete valuation ring gives $j' : O \to R'$ and a key value $u$ of pulled back sections $s'$ on a pullback $x'$ of $x_O$. Then $j' \circ j$ is injective and local, and $x'$ is a pullback of $x$ along it. $\square$

The genericity is over the residue field $k$, which may have characteristic $p \neq 0$. This is why the fact on transversal zeros of generic sections is used over an arbitrary field.

**Lemma 2.9.5 (Key values over the complex numbers).** Assume the laws and descent to countable fields. Let $x$ be a key input over $\mathbb{C}$ of dimension $g$ and let $(n, l, l', \alpha)$ be admissible for $g$ with $P \geq 1$. Then some sections of $L^n$ have a key value.

Lean: `GlobalTheory.KaExists.exists_kaVal_complex`.

*Proof.* Let $x$ be a pullback of $x_0$ over a countable subfield $K_0 \subseteq \mathbb{C}$. A transcendence basis of $\mathbb{C}$ over $K_0$ is uncountable, since $\mathbb{C}$ is uncountable and algebraic over $K_0(B)$; so there is $T \in \mathbb{C}^I$ algebraically independent over $K_0$. The sections with coordinates $T$ in the pullback of a basis over $K_0$ meet transversally, and a key value exists since $P \neq 0$ in $\mathbb{C}$. $\square$

**Theorem 2.9.6 (The key invariant).** Assume the laws, the uniformization theorem, the algebraicity of tori and descent to countable fields. Then the key invariant statement holds: for every $g \geq 1$ and every prime $p$ there are $c, M \geq 1$ with $p \nmid M$ and a key invariant rule of dimension $g$, weight $c$ and level $M$.

Lean: `GlobalTheory.KaExists.kaSt` (also `GlobalTheory.T.exists_integralKeyInvariantRule_charZero`, a second name).

*Proof.* Take the numerical data of the lemma, with $M = P$ and $c$ as there. For $x$ of dimension $g$ over $K$, let $\kappa(x)$ be the unit of [the independence of the sections](/entry/ka-val-independent/): every key value of every tuple of sections on every pullback of $x$ to an algebraically closed field $K'$ along $f$ is $f(\kappa(x))$, and some pullback has a key value. In other dimensions put $\kappa(x) = 1$. In particular every key value on $x$ itself equals $\kappa(x)$.

Weight. Let $x'$ be obtained from $x$ by $(a, m)$, and take a pullback $x_1$ of $x$ along $f : K \to K'$ with a key value. Pullbacks of $x$ and $x'$ along $f$ can be chosen on one abelian variety, as key inputs $y$ and $y'$ with $y'$ obtained from $y$ by $(f(a), m_1)$ and $\det m_1 = f(\det m)$. Then $y$ is a pullback of $x_1$ along the identity of $K'$, so by base change $y$ has sections $s_1$ with a key value $\kappa_1$. The scaling property of key values gives a key value $\kappa_2$ of $s_1$ on $y'$ with $f(a)^{8c}\kappa_2 = f(\det m)^{4c}\kappa_1$. By independence $\kappa_1 = f(\kappa(x))$ and $\kappa_2 = f(\kappa(x'))$, and the law follows since $f$ is injective.

Base change. Let $x'$ be a pullback of $x$ along $f$, and let $x''$ be a pullback of $x'$ along $f' : K' \to K''$ with a key value $\kappa''$. Then $x''$ is a pullback of $x$ along $f' \circ f$. Independence for $x'$ and for $x$ gives $\kappa'' = f'(\kappa(x'))$ and $\kappa'' = f'(f(\kappa(x)))$, and $f'$ is injective.

Integrality. Let $R$, $x$ be as in the property, with $M = P$ a unit. The lemma over a discrete valuation ring gives $R'$, $j$, $x'$ and a key value $u$. Let $f : R' \to K$ and let $x_K$ be a pullback of $x$ along $f \circ j$. Then $x_K$ is a pullback of $x'$ along $f$, so by base change $f(u)$ is a key value on $x_K$, and $\kappa(x_K) = f(u)$.

Holomorphy. Let $(a, b)$ be a half characteristic, and let $q \in \mathcal{D}_g$, with $\tau(q) = \frac12(q + q^{T})$. There is a key input $x_0$ over $\mathbb{C}$ normal at $(\tau(q), 1, a, b, 1)$, so a theta witness, and by the lemma over $\mathbb{C}$ it has a key value. [The local holomorphy theorem](/entry/ka-val-locally-holomorphic/) gives an open $W \ni q$ in $\mathcal{D}_g$ and a holomorphic $V$ on $W$ such that every theta witness at $\tau(q')$, for $q' \in W$, has a key value $V(q')$, so its key invariant is $V(q')$. Hence for each $\tau$ in the Siegel space all key inputs normal at $(\tau, 1, a, b, 1)$ have the same key invariant; let $U(\tau)$ be this value, and $U(\tau) = 0$ for other $\tau$. Near each $q \in \mathcal{D}_g$, $U(\tau(q')) = V(q')$, so $U$ is holomorphic on the Siegel space. $\square$

**Remark 2.9.7.** Integrality holds after the extension $R \to R'$, and the unit $u$ lives in $R'$, not in $R$. The extension is needed because the transversal zeros and the points of the theta comparisons are defined only over $R'$. The passage to a unit of $R$, and to fields that are not algebraically closed, is part of the normalization in the next section. The level $M = P$ is not a unit at the primes that divide $P$; the next section removes this restriction by comparing the rules for two primes.

**Remark 2.9.8 (Formalization).** The proof is in [ExistsIntegralKeyInvariantRuleCharZero.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsIntegralKeyInvariantRuleCharZero.lean#L160), and the definitions are in [KaRuleK.lean](lean:Development/AbelianVarietyTheory/Definitions/KeyFormula/KaRuleK.lean#L18). The hypotheses are `ThetaUnifAV`, `TorusAlgebraic` and `KeyDesc`, and the normal key inputs come from `KeyOfPeriod.exists_keyIn_normalAt`. The scaling property is `KaScale.kaVal_scale`, the pair of pullbacks is `KeyGalDesc.exists_keyPB_pair`, and the complete ring of the lemma over a discrete valuation ring is `exists_complete_discreteValuationRing_with_residues`; we used their statements. The invariant is set to $1$ off dimension $g$ (line 174), and $U$ is set to $0$ off the Siegel space (line 231). A rule is defined only over algebraically closed fields. The lemma `exists_coords` (line 46) repeats lemmas of the same name in other files of the folder. The second name is proved by a `first | exact … | …` block, under a raised heartbeat limit ([ExistsIntegralKeyInvariantRuleCharZeroStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsIntegralKeyInvariantRuleCharZeroStatement.lean#L21)).
