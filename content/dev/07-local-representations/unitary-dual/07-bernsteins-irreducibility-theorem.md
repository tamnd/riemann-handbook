---
title: Bernstein's irreducibility theorem
decls:
  - PositivityTheory.RgUd.Prod.Final.bern_of
  - PositivityTheory.RgUd.All.bernAt
  - PositivityTheory.RgUd.All.bernsteinUnitaryProductIrreducible
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bernstein's irreducibility theorem

This section proves that the parabolic induction of two irreducible unitarisable representations of general linear groups over a nonarchimedean local field is irreducible. The proof uses three inputs from the earlier sections: the [Leibniz rule](/entry/leibniz-ord/) for derivatives of a product, and the two theorems on the top and lower derivatives of a unitarisable representation, which come from the [lift of forms](/entry/u-lift/) and [Theorem B](/entry/thm-b/). The theorem is used in step [EveryCharacter](/step/every-character/), where it makes the local components of unitary automorphic representations of $\mathrm{GL}_N$ into irreducible products. It also shows that the unitary dual of $\mathrm{GL}_N(k)$ is closed under the product $\times$, which is the first step of Tadić's classification.

Background: [parabolic induction](/learn/representations/#parabolic-induction-and-the-jacquet-module), [smooth representations of $p$-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups), [[unitary representation|74BPYJNZTM]].

### Statement

Let $k$ be a nonarchimedean local field, and let $\nu = |\det|$ on each $\mathrm{GL}_m(k)$. For smooth representations $\pi_1$ of $\mathrm{GL}_r(k)$ and $\pi_2$ of $\mathrm{GL}_t(k)$, let $\pi_1 \times \pi_2$ be the normalized parabolic induction of $\pi_1 \otimes \pi_2$ from the standard parabolic subgroup of type $(r, t)$. Fix a nontrivial continuous additive character $\psi$ of $k$, and let $\pi^{(j)}$ be the $j$-th derivative relative to $\psi$, as in [the section on derivatives](/entry/leibniz-ord/).

**Theorem 7.7.1 (Bernstein).** Let $\pi_1$ and $\pi_2$ be smooth, irreducible and unitarisable representations of $\mathrm{GL}_r(k)$ and $\mathrm{GL}_t(k)$. Then $\pi_1 \times \pi_2$ is irreducible.

Lean: `PositivityTheory.RgUd.All.bernAt` (also `PositivityTheory.RgUd.Prod.Final.bern_of`).

The published form of the theorem quantifies over the field.

**Corollary 7.7.2 (All local fields).** The statement of the theorem holds for every nonarchimedean local field $k$, of characteristic $0$ or $p$.

Lean: `PositivityTheory.RgUd.All.bernsteinUnitaryProductIrreducible`.

*Proof.* Fix $k$ and apply the theorem. The theorem uses Theorem B, which comes from [Theorem T](/entry/all-thm-t/) for $k$. Theorem T is proved separately in [characteristic zero](/entry/t-final-thm-t/) and in [characteristic $p$](/entry/tp-final-thm-t/), and every local field has one of these characteristics. $\square$

By induction on the number of factors, a product $\pi_1 \times \dots \times \pi_m$ of irreducible unitarisable representations is irreducible, since such a product is again unitarisable.

### Inputs

Let $\pi$ be a nonzero smooth representation of $\mathrm{GL}_N(k)$. Its *highest derivative* is the largest $h$ with $\pi^{(h)} \ne 0$. It exists since $\pi^{(j)} = 0$ for $j > N$. Write $h(\pi)$ for it. Three facts from earlier sections are used.

1. *Leibniz rule.* For each $\ell$ the derivative $(\pi_1 \times \pi_2)^{(\ell)}$ has a filtration whose nonzero layers are $\pi_1^{(i)} \nu^{(\ell-i)/2} \times \pi_2^{(\ell-i)} \nu^{i/2}$ for $0 \le i \le \ell$.
2. *Top derivative.* If $\pi$ is irreducible and unitarisable with $h = h(\pi) \ge 1$, then $\pi^{(h)} \nu^{(1-h)/2}$ is irreducible and unitarisable.
3. *Lower derivatives.* If $\pi$ is irreducible and unitarisable, $1 \le i < h(\pi)$, and $\sigma$ is a nonzero subquotient of $\pi^{(i)} \nu^{(1-i)/2}$ with central character $\omega$, then $|\omega(z)| < 1$ for $|z| < 1$.

Four general facts are also used. The derivative functors are exact. The derivatives of an admissible representation are locally finite for the action of the centre. In a locally finite representation, an eigenvector of a scalar matrix generates a subrepresentation with a central character that takes the same value at that scalar. And an eigenvalue of a scalar on a product, or on a filtered representation, is an eigenvalue on one of the factors, or on one of the layers.

### The two properties of a product

Let $\pi_1$ and $\pi_2$ be as in the theorem, $X = \pi_1 \times \pi_2$, $h_1 = h(\pi_1)$ and $h_2 = h(\pi_2)$. Put $\sigma_l = \pi_l^{(h_l)} \nu^{(1-h_l)/2}$ when $h_l \ge 1$, and $\sigma_l = \pi_l$ when $h_l = 0$. Then $h_l = 0$ only when $\pi_l$ is a representation of the trivial group.

**Proposition 7.7.3 (Top derivative of a product).** Assume $r + t > 0$, and let $h = h_1 + h_2$. Then $h > 0$, $h(X) = h$, and
$$X^{(h)} \cong (\sigma_1 \times \sigma_2)\, \nu^{(h-1)/2}.$$
The representations $\sigma_1$ and $\sigma_2$ are irreducible and unitarisable.

*Proof.* A nonzero smooth representation of $\mathrm{GL}_m(k)$ with $m \ge 1$ has a nonzero derivative of positive order, so $h_l \ge 1$ when the rank is positive, and $h > 0$. Apply the Leibniz rule with $\ell = h$. The layer with index $i$ is $\pi_1^{(i)} \nu^{(h-i)/2} \times \pi_2^{(h-i)} \nu^{i/2}$. If $i > h_1$ the first factor is zero, and if $i < h_1$ then $h - i > h_2$ and the second factor is zero. So only the layer $i = h_1$ is nonzero, and $X^{(h)} \cong \pi_1^{(h_1)} \nu^{h_2/2} \times \pi_2^{(h_2)} \nu^{h_1/2}$. Since $\tfrac{h_2}{2} - \tfrac{1-h_1}{2} = \tfrac{h-1}{2}$ and the same holds with the indices exchanged, this is the stated twist of $\sigma_1 \times \sigma_2$. It is nonzero, so $h(X) \ge h$. For $\ell > h$ every layer has $i > h_1$ or $\ell - i > h_2$, so $X^{(\ell)} = 0$. The last claim is the theorem on the top derivative, applied to $\pi_1$ and $\pi_2$. $\square$

**Proposition 7.7.4 (Eigenvalue bound).** Let $h = h(X)$, let $j < h$ and $n' = r + t - j$. Let $x \in k^\times$ with $|x| < 1$, and let $c$ be an eigenvalue of the scalar matrix $x$ on $X^{(j)}$. Then
$$|c| < |x|^{n'(j-1)/2}.$$

*Proof.* By the Leibniz rule and the general facts, $c$ is an eigenvalue on a layer, so $c = c_A c_B$ where $c_A$ is an eigenvalue of $x$ on $\pi_1^{(i)} \nu^{(j-i)/2}$ and $c_B$ an eigenvalue of $x$ on $\pi_2^{(j-i)} \nu^{i/2}$, for some $i$.

First bound $c_A$. Let $m = r - i$ and $s = (j-i)/2$. If $i = 0$, then $c_A |x|^{-ms}$ is an eigenvalue on the unitarisable $\pi_1$, so it has norm $1$. If $i \ge 1$, then $c_A |x|^{-ms - m(1-i)/2}$ is an eigenvalue on $\pi_1^{(i)} \nu^{(1-i)/2}$. It is the value at $x$ of the central character of a nonzero subrepresentation. When $i < h_1$, the theorem on lower derivatives makes its norm smaller than $1$. When $i = h_1$, that representation is unitarisable and its norm is $1$. In each case
$$|c_A| \le |x|^{m(s + (i-1)/2)},$$
and equality holds only if $i$ is the highest derivative of $\pi_1$, or $i = 0$ and $r = 0$. In the same way $|c_B| \le |x|^{m'(s' + (j-i-1)/2)}$, with $m' = t - (j - i)$ and $s' = i/2$, and equality forces $j - i = h_2$. A short computation gives
$$m\Big(\frac{j-i}{2} + \frac{i-1}{2}\Big) + m'\Big(\frac{i}{2} + \frac{j-i-1}{2}\Big) = (m + m')\frac{j-1}{2} = \frac{n'(j-1)}{2}.$$
So $|c| \le |x|^{n'(j-1)/2}$. If equality holds, both bounds are equalities. Then all derivatives of $\pi_1$ of order larger than $i$ vanish, and all derivatives of $\pi_2$ of order larger than $j - i$ vanish. But $X^{(h)} \ne 0$, so some layer $i'$ of the Leibniz filtration of $X^{(h)}$ is nonzero, with $\pi_1^{(i')} \ne 0$ and $\pi_2^{(h-i')} \ne 0$. Since $h > j$, either $i' > i$ or $h - i' > j - i$, which is a contradiction. $\square$

### The induction

*Proof of the theorem.* We use strong induction on $N = r + t$. If $N = 0$, both groups are trivial and $X$ is one-dimensional. Let $N > 0$ and let $h = h(X)$. By the first proposition, $X^{(h)}$ is a twist of $\sigma_1 \times \sigma_2$, a product of two irreducible unitarisable representations of total rank $N - h < N$. By induction it is irreducible.

The representation $X$ is admissible, as a product of admissible representations, and unitarisable, as the induction of a unitary representation. Fix an invariant inner product on $X$. The orthogonal complement of a subrepresentation $S$ is a subrepresentation $T$ with $X = S \oplus T$, by admissibility: each space of fixed vectors under a compact open subgroup is finite-dimensional, so the orthogonal projection exists on it. For the same reason, every nonzero subrepresentation contains an irreducible one.

*Step 1.* Let $S_0$ be a nonzero irreducible subrepresentation of $X$. We show $S_0^{(h)} \ne 0$. Let $j = h(S_0)$. Then $j \ge 1$, since $N > 0$. The derivative is exact and $S_0$ is a direct summand, so $S_0^{(l)}$ is a direct summand of $X^{(l)}$ for each $l$. If $j > h$, then $X^{(j)} \ne 0$, against $h = h(X)$. Assume $j < h$, and choose $x$ with $|x| < 1$. The representation $S_0$ is irreducible and unitarisable, as a subrepresentation of $X$. By the theorem on the top derivative, $S_0^{(j)} \nu^{(1-j)/2}$ is irreducible and unitarisable. It therefore has a unitary central character, and the scalar $x$ acts on $S_0^{(j)}$ with an eigenvalue $c$ of norm exactly $|x|^{n'(j-1)/2}$, where $n' = N - j$. An eigenvector of $c$ in $S_0^{(j)}$ is also an eigenvector in $X^{(j)}$. This contradicts the eigenvalue bound. So $j = h$.

*Step 2.* Let $S$ be a nonzero subrepresentation of $X$. It contains a nonzero irreducible $S_0$, and $S_0$ is a direct summand of $X$ contained in $S$. So $S_0^{(h)}$ injects into $S^{(h)}$, and $S^{(h)} \ne 0$ by step 1.

*Step 3.* Assume that $X = S \oplus T$ with $S$ and $T$ both nonzero. Then $X^{(h)} = S^{(h)} \oplus T^{(h)}$ by exactness, and both summands are nonzero by step 2. The image of $S^{(h)}$ is a subrepresentation of $X^{(h)}$ that is neither $0$ nor everything. This contradicts the irreducibility of $X^{(h)}$, which is not changed by a twist. So every subrepresentation of $X$ is $0$ or $X$, and $X$ is irreducible. $\square$

The argument does not use the classification of the unitary dual. It uses only the forms on derivatives, through the theorems on top and lower derivatives, and the combinatorics of the Leibniz rule. The equality case of the eigenvalue bound is the place where the highest derivatives of $\pi_1$ and $\pi_2$ enter.

**Remark 7.7.5 (Formalization).** The theorem for one field is in [BernAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/BernAll.lean#L23), and the version for all fields at line 27 of the same file. The statement for all fields is defined in [BernsteinUnitaryProductIrreducible.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/BernsteinUnitaryProductIrreducible.lean#L10). The statements of the theorem and of the theorems on top and lower derivatives are in [IsInvForm.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/IsInvForm.lean#L74). The assembly from the three inputs is in [BernOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CentralProducts/BernOf.lean#L14); it also proves the four general facts, which enter as hypotheses of the two propositions. The two propositions are stated in [TopProdD.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CentralProducts/TopProdD.lean#L42). The eigenvalue bound is proved in [PosProdOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CentralProducts/PositiveProducts/PosProdOf.lean#L89), and the top derivative of a product in [LeOfSubsingletonSubQuot.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CentralProducts/SubquotientBounds/LeOfSubsingletonSubQuot.lean#L374), a file named after a small lemma. That proof takes the theorem on lower derivatives and three of the general facts as hypotheses but does not use them. The induction and its three steps are in [NormEqOneOfUnitarisable.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CentralProducts/UnitarisableHypotheses/NormEqOneOfUnitarisable.lean#L260), with the final assembly at line 295. The file [ThmBChar0.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/ThmBChar0.lean#L13) has a second copy of the theorem for fields of characteristic zero only. The fact on central characters is proved twice, in [CentralSubGen.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CentralProducts/CentralGenerators/CentralSubGen.lean#L134) and in a one-line wrapper in [CentralSub.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CentralProducts/CentralSub.lean#L5).
