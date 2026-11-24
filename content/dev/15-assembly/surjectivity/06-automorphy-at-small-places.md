---
title: Automorphy at small places
decls:
  - frame_embedding_exists
  - GlobalTheory.T.small_place_prime_local_alt
  - GlobalTheory.FrameAut.autSt_of_smallSt'
  - GlobalTheory.T.aut_statement_of_small_exponent_statement
  - GlobalTheory.FrameAut.frame_autSt_of_smallSt
  - GlobalTheory.T.frame_aut_of_small_estimate
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Automorphy at small places

This section attaches to each eigensystem of a frame at a small place an automorphic representation of a definite [[unitary group|0R9R0Y1HDK]] in $N_r$ variables. The representation has the weights of the eigensystem at the infinite places, it is unramified above $\ell$, and its Satake parameters at the places of the block give the eigenvalues of the eigensystem. The statement holds with no published input: the automorphic forms are functions on a finite double coset space, and the frame gives them directly. [The Galois statement of Section 7](/entry/galois-steinberg-local-alt/) uses the result. The background on [unitary groups](/learn/groups/#unitary-groups) and on [unramified representations](/learn/representations/#unramified-representations) is in Volume 1.

Keep the notation of Section 5. Let $p$ be a point, $j$ a level, $(P, W)$ a dictionary pair and $w$ a twisted place with residue characteristic $\ell$, and $t = \mu(w)$. Let $V_j$ be the definite hermitian space of level $j$ over the host field $E$, of rank $N = N_r$. Let $U_N$ be the unitary group of the standard definite form in $N$ variables over $E$, and write $\mathcal{A}(U_N)$ for the functions on $U_N(\mathbb{A})$ with values in $\mathbb{C}$. For a place $Q$ of the block, $\lambda_Q$ is the split place of $E$ above it, $q_Q$ its norm, and $K_Q = \mathrm{GL}_N(\mathcal{O}_{E, \lambda_Q})$ the maximal compact subgroup at $\lambda_Q$.

**Definition 5.6.1 (Places of a block).** The places of the block at $(j, t)$ are *good for $\ell$* if:

1. for each $Q$, the place $\lambda_Q$ is split, it lies over the same place of the maximal real subfield as $Q$, its norm is $q_Q$, and $\ell \in \lambda_Q$ if and only if $\ell \in Q$;
2. the set of places $v$ of $E$ of prime norm that are not $\lambda_Q$ for a block place $Q$ prime to $\ell$ is finite;
3. for each block value $\nu$ and each $Q$, $|\nu(Q)|^2 = q_Q^{\,n - t}$, where $n$ and $t$ are the sizes of the block.

Lean: `GlobalTheory.FrameAut.PlacesOk`.

**Definition 5.6.2 (Automorphic system).** Let $F$ be a frame of rank $N$ at $\ell$, tied to the point, with tie $T$, isomorphism $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ and shifts $s_\tau$. Let $\mu_\tau$ be weights for the infinite types $\tau$ and $\theta$ an eigensystem of $F$ for these weights. A subspace $\pi \subseteq \mathcal{A}(U_N)$ is an *automorphic system* for $\theta$ if:

1. $\pi$ is an automorphic representation of $U_N$;
2. for each $\tau$ there is a dominant weight $\lambda_\tau$ with $\lambda_\tau(a) = \mu_\tau(a) + s_\tau$, such that $\pi$ has weight $\lambda_\tau$ at the embedding $\iota \circ \mathrm{inc}_\tau$ and the dual weight at its conjugate;
3. $\pi$ is unramified at each place $v$ of $E$ above $\ell$;
4. for each block place $Q$, $\pi$ is unramified at $\lambda_Q$, and there are a smooth irreducible representation $\sigma$ of $\mathrm{GL}_N(E_{\lambda_Q})$ and a multiset $S$ of $N$ nonzero complex numbers such that $\sigma$ is the component of $\pi$ at $\lambda_Q$, $S$ is the Satake parameter of $\sigma$, and for each index $i$ at $Q$ with Hecke index $k$, $\iota(\theta_i)$ is the eigenvalue of the $k$-th Hecke operator at $\lambda_Q$ on the spherical vector with Satake parameter $S$.

Lean: `GlobalTheory.FrameAut.IsSystemOf`.

**Definition 5.6.3 (Automorphy at a place).** The *automorphy condition* at $w$ holds if the places of the block are good for $\ell$ and, for each good frame $F$ of rank $N_r$ at $\ell$ with a reading $R$ of the block and a tie $T$, each family of weights $\mu_\tau$ with antitone residues and each eigensystem $\theta$ of $F$ for these weights, there is an automorphic system $\pi$ for $\theta$. The *automorphy statement* is the automorphy condition, in range.

Lean: `GlobalTheory.FrameAut.AutAt` (also `GlobalTheory.FrameAut.AutStAlt`).

**Lemma 5.6.4 (A form from an eigensystem).** Let $F$ be a frame of rank $N = \operatorname{rank} V_j$ tied to the point, and let $\theta$ be an eigensystem of $F$ for weights $\mu_\tau$ with antitone residues. Then there are an automorphic representation $\pi$ of $U_N$ with the weights of condition 2 above and a nonzero $\varphi \in \pi$ such that:

1. $\varphi$ is fixed by the maximal compact subgroup at each good place of the point;
2. for each block place $Q$, $\varphi$ is fixed by $K_Q$, and for each index $i$ at $Q$ with Hecke index $k$, the $k$-th Hecke operator at $\lambda_Q$ acts on $\varphi$ by $\iota(\theta_i)$.

Lean: `frame_embedding_exists`.

*Proof.* The space $V_j$ is positive definite and its signature is the one that the point fixes. So there is a transfer from the unitary group of $V_j$ to $U_N$, with an element $h_0$, and an invariant positive definite hermitian form on the coefficients. The eigensystem $\theta$ of the frame gives a nonzero vector valued eigenform on the finite set of double cosets of the level group, with the eigenvalues $\theta$ under the Hecke operators of the frame. Through the transfer it becomes a vector valued automorphic form on $U_N$ whose infinite component is equivariant for the weights $\lambda_\tau$. The scalar coefficients of this form span an automorphic representation $\pi$ of $U_N$ with the weights $\lambda_\tau$ at $\iota \circ \mathrm{inc}_\tau$; at the conjugate embedding the weight is dual, since the embeddings $\iota \circ \mathrm{inc}_\tau$ are the base embeddings of the point or their conjugates. A coefficient $\varphi \ne 0$ is fixed at the good places, since the level character is trivial there. At a block place $Q$, the off level place gives a spherical Hecke representation at the split label, and the transfer carries the Hecke operator of the frame at $Q$ to the Hecke operator at $\lambda_Q$. So $\varphi$ is a Hecke eigenvector with eigenvalue $\iota(\theta_i)$. $\square$

**Theorem 5.6.5 (Automorphic forms at small places).** Let $p$ be a regular rich point, $(P, W)$ a dictionary pair that passes the numerical checks, and $w$ a small twisted place with $W$ in range at $\ell$. Let $F$, $R$, $T$, $\mu$ and $\theta$ be as in the definition of automorphy. Then there is an automorphic representation $\pi$ of $U_{N_r}$ with the weights of condition 2, unramified at each place above $\ell$, and with a nonzero $\varphi \in \pi$ such that, for each block place $Q$ prime to $\ell$, $\varphi$ is fixed by $K_Q$ and is an eigenvector of the Hecke operators at $\lambda_Q$ with the eigenvalues $\iota(\theta_i)$.

Lean: `GlobalTheory.T.small_place_prime_local_alt`.

*Proof.* Apply the lemma with $N = N_r$, the embedding $e_0$ and index map of $R$, and the tie $T$. It gives $\pi$ and $\varphi$. A place $v$ of $E$ above $\ell$ is a good place of the point, because $w$ is twisted, the dictionary matches and $W$ is in range at $\ell$. So $\varphi$ is fixed at $v$, and $\pi$ is unramified there. The block places are covered by part 2 of the lemma. $\square$

To pass from a Hecke eigenvector to the Satake parameter we use the Satake isomorphism (Satake, 1963). For a split place $v$ of $E$ and an automorphic representation $\pi$ of $U_n$, each nonzero $\varphi \in \pi$ fixed by $\mathrm{GL}_n(\mathcal{O}_{E,v})$ lies in a component $\sigma$ of $\pi$ at $v$ with a Satake parameter $S$, and the $k$-th Hecke operator acts on $\varphi$ by the $k$-th elementary symmetric function of $S$, normalized by a power of the norm of $v$. It is a proved theorem of the development, not a hypothesis here.

**Theorem 5.6.6 (The automorphy statement).** The smallness condition implies the automorphy statement.

Lean: `GlobalTheory.FrameAut.autSt_of_smallSt'` (also `GlobalTheory.T.aut_statement_of_small_exponent_statement`, `GlobalTheory.FrameAut.frame_autSt_of_smallSt` and `GlobalTheory.T.frame_aut_of_small_estimate`, second names).

*Proof.* Let $w$ be small, in range. Five facts at $w$ give the automorphy condition.

1. The block decomposition: condition 1 of good places.
2. The finite set: condition 2 of good places.
3. The norms of the block values: $|\nu(Q)|^2 = q_Q^{\,n - t}$, condition 3.
4. The Satake isomorphism for the definite unitary group at split places, as above.
5. The theorem on automorphic forms at small places.

Given $F$, $R$, $T$, $\mu$ and $\theta$, fact 5 gives $\pi$ and $\varphi$. At each block place $Q$ prime to $\ell$, fact 4 gives the component $\sigma$ of $\pi$ at $\lambda_Q$ and its Satake parameter $S$, with the eigenvalues $\iota(\theta_i)$. So $\pi$ is an automorphic system for $\theta$. With facts 1 to 3 this is the automorphy condition at $w$. The statement holds in range with the thresholds of the smallness condition. $\square$

**Remark 5.6.7 (Formalization).** The lemma is private, in [SmallPlacePrimeLocal.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SmallPlacePrimeLocal.lean#L29), with `maxHeartbeats` set to 1600000. The theorem on automorphic forms at small places is at line 109 of the same file. Its proof does not use the smallness of $w$, the numerical checks, the point conditions or the richness of $p$: only the dictionary, the twisted place and the range condition. Condition 4 of an automorphic system asks for all block places, but the theorem gives Hecke eigenvalues only at the block places prime to $\ell$; the Galois step of Section 7 uses only those. The definitions are in [IsSystemOf.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsSystemOf.lean#L55). The automorphy statement has four names in a row: [AutStOfSmallStStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AutStOfSmallStStatement.lean#L11) calls [AutStOfSmallSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AutStOfSmallSt.lean#L10), which calls [AutAtOfStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AutAtOfStatement.lean#L11), which calls the theorem in [AutAtOf.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AutAtOf.lean#L138). The word "exponent" in one of the names says nothing about the statement. We have not unfolded the transfer, the vector valued eigenform, the Hecke operators of the frame or the normalization of the Satake parameter; the proof of the lemma above is our reading of the names of the lemmas it calls.
