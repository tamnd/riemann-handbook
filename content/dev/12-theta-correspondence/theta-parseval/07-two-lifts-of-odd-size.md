---
title: Two lifts of odd size
decls:
  - UpperTheory.Gal.TP.twoUpOK_of_k
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Two lifts of odd size

This section uses [the theta lift in the stable range](/entry/t-lift-holds-k/) to move an automorphic representation of a definite unitary group of even rank $n$ to two automorphic representations of a definite unitary group of odd rank $n + t$. The two lifts have the same twist of the old Satake parameters, and the $t$ new Satake parameters of the first lift differ from those of the second. The construction is the input of the step that [attaches Galois representations in even rank](/entry/to-core-k/): a Galois representation for the odd rank group contains the twisted Galois representation of the even rank group plus $t$ characters, and with two lifts whose extra characters are disjoint, the common part is the representation that we want. The local input is the classical computation of the unramified theta correspondence at split places (Rallis 1982), where the dual pair is $(GL_n, GL_{n+t})$ and the lift adds a segment of characters to the Satake parameters.

Let $E$ be a CM field with maximal real subfield $F$. In this section $U(n)$ is the definite unitary group of the standard Hermitian form of rank $n$ for $E/F$, and an automorphic representation of $U(n)$ is a space of functions on $U(n)(\mathbb{A}_F)$ as in [the theta lift section](/entry/t-lift-of-tools-k/). A finite place $w$ of $E$ is *split* if $w$ lies over a place of $F$ that splits in $E$; at a split place $U(n)(F_v) \cong GL_n(E_w)$, and an unramified local component has a Satake parameter, a multiset $B$ of $n$ nonzero complex numbers.

**Definition 6.7.1 (Good inert places).** The field $E$ has *good inert places* if for each finite place $w$ of $E$ that is not split, the place $v$ of $F$ below $w$ does not divide $2$, its norm is greater than $3$, and $v$ does not divide the different of $F$ over $\mathbb{Q}$.

**Definition 6.7.2 (Weight jumps and algebraic normalization).** For a dominant weight $\lambda = (\lambda_0 \ge \dots \ge \lambda_{n-1})$ of $U(n)$ the *weight jumps* are the multiset $\{ k - \lambda_k : 0 \le k < n \}$. For a Satake parameter $B$ of rank $n$ at a place with residue field of size $q$, the *algebraic normalization* is the multiset $q^{(n-1)/2} B$.

The weight jumps are the Hodge-Tate weights that the Galois representation of the automorphic representation should have, and the algebraic normalization is the normalization of Satake parameters that matches the eigenvalues of Frobenius.

**Definition 6.7.3 (Up lift).** Let $U$ be an automorphic representation of $U(n)$ with weights $\lambda_\tau$ for each embedding $\tau \colon E \to \mathbb{C}$. Let $\kappa$ be an algebraic [Hecke character](/learn/class-field-theory/#hecke-characters) of $E$ of infinity type $m$, and let $\psi_0, \dots, \psi_{t-1}$ be algebraic Hecke characters of $E$ of infinity types $p_0, \dots, p_{t-1}$. An automorphic representation $U'$ of $U(n + t)$ with weights $\lambda'_\tau$ is an *up lift* of $U$ for $(\kappa, \psi)$ if:

1. for each $\tau$ the weight jumps of $\lambda'_\tau$ are the weight jumps of $\lambda_\tau$ plus $m_\tau$, together with the numbers $-p_{i,\tau}$;
2. at each split place $w$ where $\kappa$ and all $\psi_i$ are unramified, for each Satake parameter $B$ of $U$ at $w$ there is a Satake parameter $B'$ of $U'$ at $w$ whose algebraic normalization is the algebraic normalization of $B$ times $\kappa(w)^{-1}$, together with the numbers $\psi_0(w), \dots, \psi_{t-1}(w)$.

So an up lift adds $t$ characters to the parameter of $U$ twisted by $\kappa^{-1}$, both at the infinite places and at the split unramified places.

**Theorem 6.7.4 (Two lifts of odd size).** Let $E$ be a CM field such that $E/F$ is unramified at all finite places, $E$ contains an element $x$ with $x^2 = -d$ for a positive integer $d$, and $E$ has good inert places. Let $n \ge 1$ be even, let $U$ be an automorphic representation of $U(n)$ with weights $\lambda_\tau$, and let $w_0$ be a split place. Then there are an odd integer $t$ with $n + t$ odd, an algebraic Hecke character $\kappa$ of infinity type $m$, and two families $\psi^{(1)}$, $\psi^{(2)}$ of $t$ algebraic Hecke characters with up lifts $U_1$ and $U_2$ of $U$ for $(\kappa, \psi^{(1)})$ and $(\kappa, \psi^{(2)})$, such that $\psi^{(1)}_i \ne \psi^{(2)}_j$ for all $i$ and $j$, and $\kappa$ and all $\psi^{(1)}_i$ are unramified at $w_0$.

Lean: `UpperTheory.Gal.TP.twoUpOK_of_k` (also `UpperTheory.Gal.TP.twoUpOK_of_steps`, the same conclusion from the four inputs below).

The proof takes four inputs: the theta lift in the stable range, and three results on base data, characters and the read-off of parameters.

**Lemma 6.7.5 (Base data).** Let $E$ be a CM field such that $E/F$ is unramified at all finite places and $E$ has good inert places. Then there are base data for $E/F$ with an unramified standard additive character, an element $\delta \in E$ and a fractional ideal $\mathfrak{a}$, such that the standard Hermitian space of each rank $n$ is definite of signature $(n, 0)$ and the skew-Hermitian space with Gram matrix $\delta \cdot 1$ and lattice $\mathfrak{a}^d$ is definite of signature $(d, 0)$ for each $d$.

Lean: `UpperTheory.Gal.TP.Sub.baseNG`.

**Lemma 6.7.6 (Character pairs).** Let $E$ be as in the lemma on base data, let $n$ be even and $t$ odd, fix embeddings over the infinite places, an integer $b$ and a split place $w_0$. Then there are an algebraic Hecke character $\kappa$ of infinity type $m$ and, for $j = 0, 1$, Hecke characters $\chi_X^{(j)}$ and $\chi_W^{(j)}$ with exponents $m_X^{(j)}$ and $m_W^{(j)}$ and $t$ algebraic Hecke characters $\psi^{(j)}_i$ of infinity types $p^{(j)}_i$, such that:

1. $\chi_X^{(j)}$ restricts to $\eta^n$ and $\chi_W^{(j)}$ restricts to $\eta^{n+t}$ on $\mathbb{A}_F^\times$, where $\eta$ is the quadratic character of $E/F$;
2. $m_{W,w}^{(j)} \le b$ for all infinite places $w$;
3. at each infinite place $w$, with $\tau_w$ the chosen embedding, $2m_{\tau_w} = m_{W,w} - m_{X,w} + t$ and $2p_{i,\tau_w} = m_{X,w} + 2i - (n + 2t - 2)$, and the formulas with the signs of $m_X$ and $m_W$ changed hold at the conjugate embedding;
4. at each place $w$ where $\kappa$ and the $\psi_i$ are unramified, $\chi_X$ and $\chi_W$ are unramified, $\kappa(w) = \chi_W(w)\chi_X(w)^{-1} q_w^{-t/2}$ and $\psi_i(w) = \chi_X(w)\, q_w^{(n + 2t - 2)/2 - i}$;
5. $\psi^{(0)}_i \ne \psi^{(1)}_{i'}$ for all $i$, $i'$, and $\kappa$ and the $\psi^{(0)}_i$ are unramified at $w_0$.

Lean: `UpperTheory.Gal.TP.Chr.chrPairs_holds`.

Conditions 3 and 4 together are the *dictionary* between the splitting characters of the Weil representation and the characters of an up lift.

**Lemma 6.7.7 (Read-off of the up lift).** Let $1 \le n < t$, and let $U'$ be a theta lift of $U$ to $U(n + t)$ in the sense of [the theta lift in the stable range](/entry/t-lift-holds-k/), for splitting characters $\chi_X$, $\chi_W$ that satisfy the dictionary with $(\kappa, \psi)$. Then $U'$ is an up lift of $U$ for $(\kappa, \psi)$.

Lean: `UpperTheory.Gal.TP.Sub.upOf`.

*Proof.* At an infinite place, the lift weight $\lambda'$ satisfies $2\lambda'_k = 2\lambda_k - (n + t) - m_W + n + m_X$ for $k < n$ and $2\lambda'_k = n + m_X$ for $k \ge n$. With $2m = m_W - m_X + t$ the first $n$ weight jumps $k - \lambda'_k$ are $k - \lambda_k + m$, and with $2p_i = m_X + 2i - (n + 2t - 2)$ the last $t$ weight jumps $n + i - \lambda'_{n+i}$ are the numbers $-p_i$ in some order. The same computation at the conjugate embedding uses the dual weights. At a split unramified place, the local components of $U$ and $U'$ are paired by the Weil representation of $GL_n \times GL_{n+t}$, and the unramified theta correspondence for this pair (Rallis 1982; Mínguez 2008) adds to the parameter of $U$, twisted by $\chi_X\chi_W^{-1}$, the segment of the $t$ characters $\chi_X \lvert\cdot\rvert^{s}$ with $s$ in an arithmetic progression of step $1$. In the algebraic normalization this is the statement of condition 2 of an up lift, with $\kappa$ and $\psi_i$ given by the dictionary. $\square$

*Proof of the theorem.* The lemma on base data gives base data, $\delta$ and $\mathfrak{a}$. With the element $x$, $x^2 = -d$, these base data are good in the sense of this chapter, so the theta lift in the stable range applies to the standard Hermitian space of rank $n$ and gives $d_0$. Put $t = 2(d_0 + n) + 1$. Then $t$ is odd, $n + t$ is odd because $n$ is even, $n + t \ge d_0$, and $n < t$. Let $b$ be a lower bound of the finite set of weights $\lambda_{\tau,k}$, and apply the lemma on character pairs with the bound $2b - (n + t)$. For $j = 0, 1$ the characters $\chi_X^{(j)}$ and $\chi_W^{(j)}$ satisfy the hypotheses of the theta lift for $d = n + t$: the weight condition $d + m_{W,w} \le 2\lambda_{w,k}$ follows from $m_{W,w} \le 2b - d$ and $b \le \lambda_{w,k}$. So there are theta lifts $U_1$ and $U_2$ of $U$ to $U(n + t)$, and by the read-off lemma they are up lifts for $(\kappa, \psi^{(0)})$ and $(\kappa, \psi^{(1)})$. Condition 5 of the lemma on character pairs gives the disjointness and the conditions at $w_0$. $\square$

The size $t$ is large so that $n + t$ is in the stable range of the theta lift for both choices of characters at once. The choice $t$ odd makes $n + t$ odd.

**Remark 6.7.8 (Formalization).** The statement assumes that the degree of $F$ over $\mathbb{Q}$ is even, and the proof does not use this hypothesis ([TwoUpOKOfSteps.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/TwoUpOKOfSteps.lean#L14)); the statement with this hypothesis is in [AllCoreOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/AllCoreOf.lean#L18). The condition on the element $x$ with $x^2 = -d$ is a hypothesis of the theorem and the base data lemma does not give it; the proof adds it to the base data by hand to get good base data. The definitions of the dictionary, the character pairs and the read-off are in [TwoUpOKOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/SplitLineSubtraction/TwoUpOKOf.lean#L28), and the up lift and the pair of up lifts are in [RowDefOfOdd.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/SplitLineSubtraction/RowDefOfOdd.lean#L98). The formal proof of the read-off lemma has four parts: the embeddings over the infinite places give all embeddings of $E$, the weight identity, the Satake identity, and the local Satake computation for the lift at split places. We have not opened these four proofs or the proofs of the other two lemmas, so the proof of the read-off lemma above gives the classical computation and not the formal one.
